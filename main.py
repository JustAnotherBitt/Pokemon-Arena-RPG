import pickle
from pessoa import *
from time import sleep


def escolher_pokemon_inicial(player):
    print(f'Olá, \033[34m{player}\033[m! Agora você escolherá o Pokémon que irá lhe acompanhar nesta jornada!')
    print()
    sleep(4)

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Você possui 3 escolhas: ')
    print()
    print('1 -', pikachu)
    print('2 -', charmander)
    print('3 -', squirtle)

    while True:
        print()
        escolha = input('\033[34mEscolha o seu Pokemon:\033[m ')

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
            print('\033[3;31mEscolha inválida\033[m')


def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:  # wb = escrever / binário
            pickle.dump(player, arquivo)
            sleep(1)
            print("\033[3;37mJogo salvo com sucesso!\033[m")
    except Exception as error:
        print('\033[3;31mErro ao salvar o jogo.\033[m')
        print(error)


def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:  # wb = leitura binária
            player = pickle.load(arquivo)  # transforma o conteúdo do arquivo no objeto player
            print('\033[3;32mLoading feito com sucesso!\033[m')
            return player
    except Exception as error:
        print('\033[37mSave não encontrado.\033[m')


# ARENA:

if __name__ == "__main__":  # executa o codigo apenas se rodar esse arquivo (main.py)
    print('-' * 46)
    print('\033[1;34mBem-vindo ao minigame Pokémon RPG de terminal!\033[m')
    print('-' * 46)

    player = carregar_jogo()

    if not player:
        nome = str(input("Qual é o seu nome? -> "))
        player = Player(nome)
        sleep(1)
        print()
        print('\033[3;32mCarregando novo mundo...\033[m')
        sleep(2)
        print()
        print(f'''Olá, \033[34m{nome}\033[m! Este é um mundo habitado por Pokémons. 
A partir de agora, sua missão é se tornar um mestre dos Pokémons.
Capture o máximo de Pokémos que conseguir e lute contra seus inimigos!''')
        print()
        sleep(5)
        player.mostrar_dinheiro()

        if player.pokemons:
            print()
            print('Já vi que você tem alguns pokemons...')
            sleep(2)
            player.mostrar_pokemons()
        else:
            print()
            print('Você não tem nenhum Pokémon, portanto, precisa escolher um...')
            sleep(2)
            escolher_pokemon_inicial(player)

        sleep(1)
        print('Pronto! Agora que você já possui um Pokémon, enfrente seu arqui-inimigo desde seu nascimento: \033[31mGary.\033[m')
        gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
        print()
        sleep(3)
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print()
        print('O que desejas fazer?')
        print('-' * 22)
        sleep(1)
        print('''\033[34m0 - Sair do jogo
1 - Explorar o mundo
2 - Lutar com um inimigo
3 - Ver pokeagenda\033[m''')
        print('-' * 15)
        sleep(1)
        escolha = int(input('Sua escolha: '))

        if escolha == 0:
            print()
            print('\033[3;31mSaindo do jogo...\033[m')
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
            print('\033[3;31mEscolha inválida.\033[m')
