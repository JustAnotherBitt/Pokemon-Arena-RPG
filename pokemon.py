import random
class Pokemon: #classe pai

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1,100)

        if nome:
            self.nome = nome
        else: #se o pokemon não tiver nome, o nome dele será a espécie
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return f'{self.especie} ({self.level})'

    def atacar(self, pokemon):
        ataque_efetivo = int((self.ataque * random.random() * 1.3))
        pokemon.vida -= ataque_efetivo
        print(f'\033[1;31m{pokemon} perdeu {self.ataque} pontos de vida\033[m')

        if pokemon.vida <= 0:
            print(f'\033[31m{pokemon} foi derrotado\033[m')
            return True
        else:
            return False

class PokemonEletrico(Pokemon): #pokemon eletrico = classe filha do Pokemon
    tipo = "elétrico"

    def atacar(self, pokemon):
        print(f'\033[33m{self} lançou um raio em {pokemon}\033[m')
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print(f'\033[33m{self} lançou uma bola de fogo na cabeça de {pokemon}\033[m')
        return super().atacar(pokemon)

class PokemonAgua(Pokemon):  # pokemon eletrico = classe filha do Pokemon
    tipo = "água"

    def atacar(self, pokemon):
        print(f'\033[33m{self} lançou um jato de agua em {pokemon}\033[m')
        return super().atacar(pokemon)

