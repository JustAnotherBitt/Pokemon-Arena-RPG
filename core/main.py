from services.language_manager import LanguageManager
from core.player import *
from resources import colors as c
from time import sleep
import textwrap
from resources import ascii_art
from services.database import (
    save_player,
    load_player,
    init_database,
    list_saves,
    delete_player
)

# Variáveis globais controladas
t = None
idioma = None


# =========================
# FUNÇÕES AUXILIARES
# =========================

def saves_disponiveis(saves):
    print("\nSaves disponíveis:")
    for idx, save in enumerate(saves, start=1):
        print(
            f"{idx} - Jogador {c.bold_blue}{save['name']}{c.x} "
            f"({save['pokemons']} Pokémons, ${save['money']})"
        )


def escolher_pokemon_inicial(player):
    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print(textwrap.dedent(f"""
        Você possui 3 escolhas:
        1 - {pikachu}
        2 - {charmander}
        3 - {squirtle}
    """))

    while True:
        escolha = input(f'{c.blue}\nEscolha o seu Pokémon:{c.x} ').strip()

        if escolha == '1':
            player.capturar(pikachu)
            ascii_art.pikachu_ascii()
            break
        elif escolha == '2':
            player.capturar(charmander)
            ascii_art.charmander_ascii()
            break
        elif escolha == '3':
            player.capturar(squirtle)
            ascii_art.squirtle_ascii()
            break
        else:
            print(f"{c.red}{t('invalid_option')}{c.x}")


def iniciar_jogo():
    global idioma

    name = input(t("choose_nickname") + " ").strip()
    player = Player(name)

    print(f'{c.italic_green}\n{t("loading_world")}{c.x}')
    sleep(2)

    print(textwrap.dedent(
        t("mission_intro", name=f"{c.blue}{name}{c.x}")
    ))

    sleep(2)
    player.mostrar_dinheiro()

    if player.pokemons:
        print(t("have_pokemons"))
        sleep(1)
        player.mostrar_pokemons()
    else:
        print(textwrap.dedent(t("pokemon_master_first_step")))
        sleep(1)
        escolher_pokemon_inicial(player)

    rival_colored = f"{c.red}Gary{c.x}"
    print(textwrap.dedent(
        t("everything_settled_up", rival=rival_colored)
    ))

    gary = Inimigo(name='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
    sleep(1)
    player.batalhar(gary)

    save_player(idioma, player.name, player.to_dict())
    return player


def bye():
    print(f'{c.red}\n{t("menu_exit")}{c.x}')
    sleep(1)
    print(f'{c.red}{t("goodbye")}{c.x}')
    ascii_art.bye_ascii()


# =========================
# LOOP PRINCIPAL
# =========================

def main():
    global t, idioma

    init_database()

    # Seleção de idioma
    while True:
        idioma_input = input("Choose your language (pt/en): ").strip().lower()

        if idioma_input not in ["pt", "en"]:
            print(f"{c.red}Invalid language. Please choose 'pt' or 'en'.{c.x}")
            continue

        idioma = idioma_input
        lang = LanguageManager(idioma)
        t = lang.get
        break

    player = None

    # Menu inicial
    while player is None:

        print(textwrap.dedent(f"""
            {t("welcome_title")}
            
            {t("menu_load")}
            {t("menu_new")}
        """))

        opcao = input(t("choose_option") + " ").strip()

        if opcao == "1":

            while True:
                saves = list_saves(idioma)

                if not saves:
                    print(f"{c.red}Nenhum save encontrado para o idioma selecionado.{c.x}")
                    nova = input(f"{c.blue}Deseja começar nova jornada? [S/N]{c.x} ").strip().upper()

                    if nova == "S":
                        player = iniciar_jogo()
                        break
                    elif nova == "N":
                        bye()
                        return
                    else:
                        print(f"{c.red}{t('invalid_option')}{c.x}")
                        continue

                saves_disponiveis(saves)

                escolha = input(
                    '\nEscolha um save pelo número '
                    '(escreva "delete" para apagar ou "exit" para sair): '
                ).strip()

                if escolha.isdigit():
                    indice = int(escolha) - 1

                    if 0 <= indice < len(saves):
                        escolhido = saves[indice]
                        player = Player.from_dict(escolhido["data"])
                        print(f"\n{c.green}✅ Progresso carregado com sucesso!{c.x}")
                        break
                    else:
                        print(f"{c.red}{t('invalid_option')}{c.x}")

                elif escolha == "delete":
                    delete_option = input("Qual número deseja apagar? ").strip()

                    if delete_option.isdigit():
                        indice = int(delete_option) - 1

                        if 0 <= indice < len(saves):
                            nome = saves[indice]["name"]

                            confirm = input("Tem certeza? [S/N] ").strip().upper()
                            if confirm == "S":
                                delete_player(idioma, nome)
                                print(f"\n{c.green}Save apagado com sucesso!{c.x}")
                            continue

                    print(f"{c.red}{t('invalid_option')}{c.x}")

                elif escolha == "exit":
                    bye()
                    return

                else:
                    print(f"{c.red}{t('invalid_option')}{c.x}")

        elif opcao == "2":
            player = iniciar_jogo()

        else:
            print(f"{c.red}{t('invalid_option')}{c.x}")

    # =========================
    # ARENA LOOP
    # =========================

    while True:

        print("=" * 28)
        print(textwrap.dedent(f"""
            {c.blue}0 - Sair do jogo
            1 - Explorar o mundo
            2 - Lutar contra um inimigo
            3 - Ver Pokéagenda
            4 - Ver carteira
            5 - Conquistas alcançadas{c.x}
        """).strip())
        print("=" * 28)

        entrada = input("Sua escolha: ").strip()

        if not entrada.isdigit():
            print(f"{c.red}{t('invalid_option')}{c.x}")
            continue

        escolha = int(entrada)

        if escolha == 0:
            bye()
            return

        elif escolha == 1:
            player.explorar()

        elif escolha == 2:
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)

        elif escolha == 3:
            player.mostrar_pokemons()

        elif escolha == 4:
            player.mostrar_dinheiro()

        elif escolha == 5:
            player.mostrar_conquistas()

        else:
            print(f"{c.red}{t('invalid_option')}{c.x}")
            continue

        # salva automaticamente após ações relevantes
        save_player(idioma, player.name, player.to_dict())


# =========================

if __name__ == "__main__":
    main()
