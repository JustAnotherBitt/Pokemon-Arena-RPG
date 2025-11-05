from pessoa import *
import colors as c
from time import sleep
import textwrap
import ascii_art
from database import save_player, load_player, init_database, list_saves, delete_player

# Inicializa o banco de dados (cria a tabela se não existir)
init_database()

def saves_disponiveis():
    print("\nSaves disponíveis:")
    for idx, save in enumerate(saves, start=1):
        print(f"{idx} - Jogador {c.bold_blue}{save['name']}{c.x} ({save['pokemons']} Pokémons, ${save['money']})")


def iniciar_jogo():
    name = input("Escolha um nickname incrível: ").strip()
    player = Player(name)
    print(f'{c.italic_green}\nCarregando novo mundo...{c.x}')
    sleep(2)

    print(textwrap.dedent(f'''
        Olá, {c.blue}{name}{c.x}! Este é um mundo habitado por Pokémons. 
        A partir de agora, sua missão é se tornar um mestre dos Pokémons!
        Capture o máximo de Pokémons que conseguir e lute contra seus inimigos!
    '''))
    sleep(3)
    player.mostrar_dinheiro()

    if player.pokemons:
        print('\nVi que você já possui alguns Pokémons...')
        sleep(1)
        player.mostrar_pokemons()
    else:
        print(textwrap.dedent(f'''
            O primeiro passo para se tornar um mestre de Pokémons começa agora! 
            Escolha seu parceiro de batalha!
        '''))
        sleep(1)
        escolher_pokemon_inicial(player)

    print(textwrap.dedent(f'''
        Tudo pronto! 
        Com seu primeiro Pokémon em mãos, é hora de encarar seu rival de longa data: {c.red}Gary.{c.x}
        Mostre do que você é capaz!
    '''))
    gary = Inimigo(name='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
    sleep(1)
    player.batalhar(gary)
    save_player(idioma, player.name, player.to_dict())

    return player


def bye():
    print(f'{c.red}\nSaindo do jogo...{c.x}')
    sleep(1)
    print(f'{c.red}Goodbye!{c.x}')
    ascii_art.bye_ascii()
    

def escolher_pokemon_inicial(player):
    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print(textwrap.dedent(f'''
        Você possui 3 escolhas:
        1 - {pikachu}
        2 - {charmander}
        3 - {squirtle}
        '''))

    while True:
        escolha = input(f'{c.blue}\nEscolha o seu Pokémon:{c.x} ')

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
            print(f'{c.italic_red}Escolha inválida.{c.x}')


# ARENA:

if __name__ == "__main__":
    idioma = "pt"
    
    print(textwrap.dedent(f'''
        Bem-vindo ao Pokémon Arena RPG!
        
        1 - Carregar jogo existente
        2 - Começar nova jornada
    '''))

    opcao = input("O que você deseja fazer? ").strip()

    if opcao == "1":
        while True:
            saves = list_saves(idioma)

            if not saves:
                print(f"{c.red}Nenhum save encontrado para o idioma selecionado.{c.x}")
                while True: 
                    começar_jornada = input(f"{c.blue}Deseja começar nova jornada? [S/N]{c.x} ").strip().upper()
                    if começar_jornada == "S":
                        player = iniciar_jogo()
                        break
                    elif começar_jornada == "N":
                        bye()
                        exit()
                    else:                
                        print(f"\n{c.italic_red}Erro{c.x}") 
                break  # sai do while True após iniciar ou sair do jogo

            saves_disponiveis()

            escolha = input('\nEscolha um save pelo número (escreva "delete" para apagar um save ou "exit" para sair do jogo): ').strip()

            if escolha.isdigit() and 1 <= int(escolha) <= len(saves):
                escolhido = saves[int(escolha) - 1]
                player = Player.from_dict(escolhido["data"])
                print(f"\n{c.green}✅ Progresso carregado com sucesso!{c.x}")
                break  # salva carregado com sucesso, sai do loop principal

            elif escolha == "delete":    
                delete_option = input("Qual save você quer apagar? ").strip()
                
                if delete_option.isdigit() and 1 <= int(delete_option) <= len(saves):
                    save = saves[int(delete_option) - 1]
                    nome = save["name"]

                    while True:
                        escolha_final = input("Tem certeza que deseja fazer isso? [S/N] ").strip().upper()

                        if escolha_final == "S":
                            delete_player(idioma, nome)
                            print(f"\n{c.green}✅ Save de '{nome}' apagado com sucesso!{c.x}")
                            break  # volta para o início do loop para atualizar os saves
                        elif escolha_final == "N":
                            break  # cancela deleção e volta pro menu de saves
                        else:
                            print(f"\n{c.italic_red}Erro{c.x}") 
                else:
                    print(f"\n{c.italic_red}Save inválido.{c.x}")
                    
            elif escolha == "exit":
                bye()
                exit()

            else:
                print(f"\n{c.italic_red}Escolha inválida.{c.x}")

    elif opcao == "2":
        player = iniciar_jogo()

    else:
        print(f"{c.red}Opção inválida.{c.x}")


    while True:
        print('\nO que desejas fazer?\n')
        print('=' * 28)
        print(textwrap.dedent(f'''
            {c.blue}0 - Sair do jogo
            1 - Explorar o mundo
            2 - Lutar contra um inimigo
            3 - Ver Pokéagenda
            4 - Ver carteira
            5 - Conquistas alcançadas{c.x}''').strip())
        print('=' * 28)
        sleep(0.5)
        escolha = int(input('Sua escolha: '))

        if escolha == 0:
            bye()
            exit()
        elif escolha == 1:
            player.explorar()
            save_player(idioma, player.name, player.to_dict())

        elif escolha == 2:
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            save_player(idioma, player.name, player.to_dict())

        elif escolha == 3:
            player.mostrar_pokemons()
        elif escolha == 4:
            player.mostrar_dinheiro()
        elif escolha == 5:
            player.mostrar_conquistas()
        else:
            print(f'{c.red}Escolha inválida.{c.x}')
