import pickle
from pessoa import *
import colors as c
from time import sleep
import textwrap


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
        print()
        escolha = input(f'{c.blue}Escolha o seu Pokémon:{c.x} ')

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print(f'{c.italic_red}Escolha inválida.{c.x}')


def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:  # wb = escrever / binário
            # noinspection PyTypeChecker
            pickle.dump(player, arquivo)
            sleep(1)
            print(f"{c.italic_gray}Jogo salvo com sucesso!{c.x}")
    except Exception as error:
        print(f'{c.italic_red}Erro ao salvar o jogo.{c.x}')
        print(error)


def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:  # wb = leitura binária
            player = pickle.load(arquivo)  # Transforma o conteúdo do arquivo no objeto player
            print(f'{c.italic_green}Loading feito com sucesso!{c.x}')
            return player
    except:
        print(f'{c.italic_gray}Save não encontrado :({c.x}')


# ARENA:

if __name__ == "__main__":
    player = carregar_jogo()

    if not player:
        nome = str(input("Escolha um nickname incrível: "))
        player = Player(nome)
        sleep(1)
        print()
        print(f'{c.italic_green}Carregando novo mundo...{c.x}')
        sleep(2)
        print()
        print(textwrap.dedent(f'''
            Olá, {c.blue}{nome}{c.x}! Este é um mundo habitado por Pokémons. 
            A partir de agora, sua missão é se tornar um mestre dos Pokémons!
            Capture o máximo de Pokémos que conseguir e lute contra seus inimigos!'''))
        print()
        sleep(3)
        player.mostrar_dinheiro()

        if player.pokemons:
            print()
            print('Vi que você já possui alguns pokemons...')
            sleep(1)
            player.mostrar_pokemons()
        else:
            print(textwrap.dedent(f'''
                O primeiro passo para se tornar um mestre de Pokémons começa agora! 
                Escolha seu parceiro de batalha!'''))
            sleep(1)
            escolher_pokemon_inicial(player)

        sleep(1)
        print(textwrap.dedent(f'''
            Tudo pronto! 
            Com seu primeiro Pokémon em mãos, é hora de encarar seu rival de longa data: {c.red}Gary.{c.x}
            Mostre do que você é capaz!'''))
        gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
        print()
        sleep(1)
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print()
        print('O que desejas fazer?')
        print('=' * 28)
        print(textwrap.dedent(f'''
            {c.blue}0 - Sair do jogo
            1 - Explorar o mundo
            2 - Lutar contra um inimigo
            3 - Ver Pokéagenda{c.x}''').strip())
        print('=' * 28)
        sleep(0.5)
        escolha = int(input('Sua escolha: '))

        if escolha == 0:
            print()
            print(f'{c.red}Saindo do jogo...{c.x}')
            print(f'{c.red}Goodbye!{c.x}')
            break
        elif escolha == 1:
            player.explorar()
            salvar_jogo(player)
        elif escolha == 2:
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == 3:
            player.mostrar_pokemons()
        else:
            print(f'{c.red}Escolha inválida.{c.x}')
