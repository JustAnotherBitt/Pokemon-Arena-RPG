from time import sleep
import colors as c
from pokemon import * # Importa todas as classes

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

    def __init__(self, nome=None, pokemons=None, dinheiro=100):  # Pokemons é uma lista
        pokemons = [] if pokemons is None else pokemons
        self.nome = nome or random.choice(NOMES)
        self.pokemons = pokemons
        self.dinheiro = dinheiro  # Dinheiro inicial

    def __str__(self):  # Característica de todas as pessoas
        return self.nome  # Quando printar uma pessoa, retorne o nome dela

    def mostrar_pokemons(self):
        if self.pokemons:
            print()
            sleep(1)
            print(f'{c.yellow}Pokemons de {self}:{c.x}')
            for index, pokemon in enumerate(self.pokemons, start=1):
                print(f'{index} - {pokemon}')
            sleep(1)
        else:
            print(f'{self} não possui nenhum pokemon.')
            sleep(1)

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{c.blue}{self} escolheu {pokemon_escolhido}.{c.x}')
            return pokemon_escolhido

        else:
            print('\033[3;31mERRO: Esse jogador não possui nenhum pokemon.{c.x}}')

    def mostrar_dinheiro(self):
        print(f'Você possui {c.green}${self.dinheiro}{c.x} em sua conta.')

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f'{c.green}Você ganhou ${quantidade}{c.x}.')
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print(f'{c.green}{self} iniciou uma batalha com {c.red}{pessoa}.{c.x}{c.x}')
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
                    print(f'{c.bold_white_green} == {self} ganhou a batalha! == {c.x}')
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                if pokemon_inimigo.atacar(pokemon):  # vitória inimiga
                    print(f'{c.bold_white_red} == {pessoa} ganhou a batalha. == {c.x}')
                    break
        else:
            print('Essa batalha não pode ocorrer...')


class Player(Pessoa):  # Player = subtipo da pessoa
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print()
        print(f'{c.green}{self} capturou {pokemon}!{c.x}')
        print()

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                try:
                    escolha = int(input('Escolha seu pokemon: '))
                    pokemon_escolhido = self.pokemons[escolha-1]
                    print()
                    print(f'{c.bold_green}{pokemon_escolhido} eu escolho você!{c.x}')
                    return pokemon_escolhido
                except:
                    print(f'{c.italic_red}Escolha inválida{c.x}')
        else:
            print('\033[3;31mERRO: Esse jogador não possui nenhum pokemon{c.x}}')

    def explorar(self):
        if random.random() <= 0.3:  # 30% de chance de isso acontecer
            pokemon = random.choice(POKEMONS)
            print()
            sleep(1)
            print(f'{c.green}Um Pokémon selvagem apareceu: {pokemon}.{c.x}')
            print()
            sleep(1)

            escolha = str(input('Deseja capturar o pokemon? [S/N] ')).upper().strip()
            if escolha == 'S':
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    sleep(1) and print(f'{c.red}Oh não! {pokemon} fugiu. Boa sorte na próxima...{c.x}')
            else:
                sleep(1) and print('Ok, boa viagem!')
        else:
            sleep(2) and print()
            print(f'{c.yellow}Essa exploração não deu em nada...{c.x}')
            print()
            sleep(1)


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:  # Se não tiver pokémons
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):  # Escolha uma qnt aleatória de pokemons aleatórios
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemons_aleatorios)  # Chama o init classe pai (Pessoa)

        else:
            super().__init__(nome=nome, pokemons=pokemons)
