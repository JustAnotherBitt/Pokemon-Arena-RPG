import random
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

    def __init__(self, nome=None, pokemons=[], dinheiro=100): # pokemons é uma lista
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro # dinheiro inicial

    def __str__(self): # característica de todas as pessoas
        return self.nome # quando printar uma pessoa, retorne o nome dela

    def mostrar_pokemons(self):
        if self.pokemons:
            print(f'Pokemons de {self}:')
            for index, pokemon in enumerate(self.pokemons):
                print(f'{index} - {pokemon}')
        else:
            print(f'{self} não tem nenhum pokemon')

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{self} escolheu {pokemon_escolhido}')
            return pokemon_escolhido
        else:
            print('ERRO: Esse jogador não poossui nenhum pokemon')

    def mostrar_dinheiro(self):
        print(f'Você possui ${self.dinheiro} em sua conta')

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f'Você ganhou ${quantidade}')
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print(f'{self} iniciou uma batalha com {pessoa}')

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f'{self} ganhou a batalha')
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                if pokemon_inimigo.atacar(pokemon): # vitória inimiga
                    print(f'{pessoa} ganhou a batalha')
                    break

        else:
            print('Essa batalha não pode ocorrer')




class Player(Pessoa): # player = subtipo da pessoa
    tipo = 'player'

    def capturar(self,pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}!')

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                try:
                    escolha = int(input('Escolha seu pokemon: '))
                    pokemon_escolhido = self.pokemons[escolha]
                    print(f'{pokemon_escolhido} eu escolho você!')
                    return pokemon_escolhido
                except:
                    print('Escolha inválida')
        else:
            print('ERRO: Esse jogador não poossui nenhum pokemon')

    def explorar(self):
        if random.random() <= 0.3: # 30% de chance de isso acontecer
            pokemon = random.choice(POKEMONS)
            print(f'Um pokemon selvagem apareceu: {pokemon}')

            escolha = str(input('Deseja capturar o pokemon? [S/N] ')).upper().strip()
            if escolha == 'S':
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print(f'{pokemon} fugiu')
            else:
                print('Ok, boa viagem')
        else:
            print('Essa exploração não deu em nada...')


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons: #se não tiver pokemons
            pokemons_aleatorios = []
            for i in range(random.randint(1,6)): #escolha uma qnt aleatória de pokoemons aleatórios
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemons_aleatorios) #chama o init classe pai (Pessoa)

        else:
            super().__init__(nome=nome, pokemons=pokemons)


