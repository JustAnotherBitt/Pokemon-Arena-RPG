import pickle
from pokemon import *
from pessoa import *
from time import sleep

def escolher_pokemon_inicial(player):
    print(f'Olá, {player}... Você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada!')

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Você possui 3 escolhas: ')
    print('1 -', pikachu)
    print('2 -',charmander)
    print('3 -', squirtle)

    while True:
        escolha = input('Escolha o seu Pokemon: ')

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha =='2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha inválida')


def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo: # wb = escrever / binário
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print('Erro ao salvar o jogo')
        print(error)

def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo: # wb = leitura binária
            player = pickle.load(arquivo) # transforma o conteúdo do arquivo no objeto player
            print('Loading feito com sucesso')
            return player
    except Exception as error:
        print('Save não encontrado')


# ARENA:

if __name__ == "__main__": # executa o codigo apenas se rodar esse arquivo (main.py)
    print('-' * 40)
    print('Bem-vindo ao minigame Pokemon RPG de terminal!')
    print('-' * 40)

    player = carregar_jogo()

    if not player:
        nome = str(input("Qual é o seu nome? -> "))
        player=Player(nome)
        print(f'Olá, {nome}, esse é um mundo habitado por pokemons. A partir de agora sua missaõ é se tornar um mestre dos pokemons')
        print('Capture o máximo de pokemos que conseguir e lute contra seus inimigos')
        player.mostrar_dinheiro()

        if player.pokemons:
            print('Já vi que você tem alguns pokemons')
            player.mostrar_pokemons()
        else:
            print('Você não tem nenhum pokemon, portanto precisa escolher um...')
            escolher_pokemon_inicial(player)

        print('Pronto! Agora que você já possui um pokemon, enfrente seu arqui-inimigo desde seu nascimento: Gary')
        gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print('-'*15)
        print('O que desejas fazer?')
        print('-' * 15)
        print('''0 - Sair do jogo
1 - Explorar o mundo
2 - Lutar com um inimigo
3 - Ver pokeagenda
        ''')
        print('-' * 15)
        escolha = int(input(('Sua escolha: ')))

        if escolha == 0:
            print('Saindo do jogo...')
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
            print('Escolha inválida')




