import random
import colors as c
from time import sleep


class Pokemon:  # Classe pai

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        self.level = level if level else random.randint(1, 100)
        self.nome = nome if nome else especie
        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return f'{self.especie} (Level {self.level})'

    def atacar(self, pokemon):
        ataque_efetivo = int((self.ataque * random.random() * 1.3))
        pokemon.vida -= ataque_efetivo
        print(f'{c.bold_red}{pokemon} perdeu {self.ataque} pontos de vida{c.x}')
        sleep(1.5)

        if pokemon.vida <= 0:
            print(f'{c.red}{pokemon} foi derrotado{c.x}')
            sleep(1.5)
            return True
        else:
            return False


class PokemonEletrico(Pokemon):  # Pokemon eletrico = classe filha do Pokemon
    tipo = "elétrico"

    def atacar(self, pokemon):
        print(f'{c.yellow}{self} lançou um raio em {pokemon}{c.x}')
        sleep(1.5)
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print(f'{c.yellow}{self} lançou uma bola de fogo na cabeça de {pokemon}{c.x}')
        sleep(1.5)
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):  # Pokemon eletrico = classe filha do Pokemon
    tipo = "água"

    def atacar(self, pokemon):
        print(f'{c.yellow}{self} lançou um jato de agua em {pokemon}{c.x}')
        sleep(1.5)
        return super().atacar(pokemon)
