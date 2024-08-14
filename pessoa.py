from time import sleep

# importar todas as classes:
from pokemon import *

NOMES = ['JogadorXP', 'RandSuper', 'RedPlayer', 'BluePlayer', 'FinMaster', 'ExtraPower', 'FullPlayer']

POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Foguinho'),
    PokemonFogo('Charmilion'),
    PokemonAgua('Squirtle'),
    PokemonAgua('Magicaro'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Raichu')
]


class Pessoa:

    def __init__(self, nome=None, pokemons=None, dinheiro=100):  # pokemons é uma lista
        if pokemons is None:
            pokemons = []
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro  # dinheiro inicial

    def __str__(self):  # característica de todas as pessoas
        return self.nome  # quando printar uma pessoa, retorne o nome dela

    def mostrar_pokemons(self):
        if self.pokemons:
            print()
            sleep(1)
            print(f'\033[33mPokemons de {self}:\033[m')
            for index, pokemon in enumerate(self.pokemons, start=1):
                print(f'{index} - {pokemon}')
            sleep(3)
        else:
            print(f'{self} não tem nenhum pokemon')
            sleep(2)

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'\033[34m{self} escolheu {pokemon_escolhido}.\033[m')
            return pokemon_escolhido

        else:
            print('\033[3;31mERRO: Esse jogador não possui nenhum pokemon\033[m')

    def mostrar_dinheiro(self):
        print(f'Você possui \033[32m${self.dinheiro}\033[m em sua conta.')

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f'\033[32mVocê ganhou ${quantidade}\033[m.')
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print(f'\033[33m{self} iniciou uma batalha com \033[31m{pessoa}.\033[m\033[m')
        sleep(1)
        pessoa.mostrar_pokemons()
        print()
        sleep(1)
        pokemon_inimigo = pessoa.escolher_pokemon()
        print()
        sleep(1)
        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f'\033[1;30;42m == {self} ganhou a batalha! == \033[m')
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                if pokemon_inimigo.atacar(pokemon):  # vitória inimiga
                    print(f'\033[1;30;41m == {pessoa} ganhou a batalha. == \033[m')
                    break

        else:
            print('Essa batalha não pode ocorrer...')


class Player(Pessoa):  # player = subtipo da pessoa
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print()
        print(f'\033[32m{self} capturou {pokemon}!\033[m')
        print()

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                try:
                    escolha = int(input('Escolha seu pokemon: '))
                    pokemon_escolhido = self.pokemons[escolha-1]
                    print()
                    print(f'\033[1;32m{pokemon_escolhido} eu escolho você!\033[m')
                    return pokemon_escolhido
                except:
                    print('\033[3;31mEscolha inválida\033[m')
        else:
            print('\033[3;31mERRO: Esse jogador não possui nenhum pokemon\033[m')

    def explorar(self):
        if random.random() <= 0.3:  # 30% de chance de isso acontecer
            pokemon = random.choice(POKEMONS)
            print()
            sleep(2)
            print(f'\033[32mUm Pokémon selvagem apareceu: {pokemon}.\033[m')
            print()
            sleep(1)

            escolha = str(input('Deseja capturar o pokemon? [S/N] ')).upper().strip()
            if escolha == 'S':
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    sleep(1)
                    print(f'\033[31mOh não! {pokemon} fugiu. Boa sorte na próxima...\033[m')
            else:
                sleep(1)
                print('Ok, boa viagem!')
        else:
            sleep(2)
            print()
            print('\033[33mEssa exploração não deu em nada...\033[m')
            print()
            sleep(1)


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:  # se não tiver pokemons
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):  # escolha uma qnt aleatória de pokemons aleatórios
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemons_aleatorios)  # chama o init classe pai (Pessoa)

        else:
            super().__init__(nome=nome, pokemons=pokemons)
