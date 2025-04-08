from time import sleep
import colors as c
import textwrap
from pokemon import * # Importa todas as classes

NOMES = ['AbyssWanderer', 'ShadowReaper', 'CrypticPhantom',
         'CyberHex', 'GlitchOverlord', 'RootPhantom', '0xDeadByte',
         'BlackenedTears', 'ArcaneDagger', 'InfernalSpecter']

POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Typhlosion'),
    PokemonFogo('Charmeleon'),
    PokemonFogo('Flareon'),
    PokemonFogo('Arcanine'),
    PokemonFogo('Blaziken'),

    PokemonAgua('Squirtle'),
    PokemonAgua('Magikarp'),
    PokemonAgua('Totodile'),
    PokemonAgua('Vaporeon'),
    PokemonAgua('Gyarados'),
    PokemonAgua('Swampert'),

    PokemonEletrico('Pikachu'),
    PokemonEletrico('Raichu'),
    PokemonEletrico('Jolteon'),
    PokemonEletrico('Electivire'),
    PokemonEletrico('Zapdos'),
    PokemonEletrico('Luxray')
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
            sleep(0.5)
            print(f'{c.yellow}Pokémons de {self}:{c.x}')
            for index, pokemon in enumerate(self.pokemons, start=1):
                print(f'{index} - {pokemon}')
            sleep(0.5)
        else:
            print(f'{self} não possui nenhum pokemon.')
            sleep(0.5)
    
    def mostrar_conquistas(self): # fix
        sleep(0.5)
        print()
        print("Função chamada")

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{c.blue}{self} escolheu {pokemon_escolhido}.{c.x}')
            return pokemon_escolhido

        else:
            print('\033[3;31mERRO: Esse jogador não possui nenhum Pokémon.{c.x}}')

    def mostrar_dinheiro(self):
        sleep(0.5)
        print()
        print(f'Você possui {c.green}${self.dinheiro}{c.x} em sua conta.')

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f'{c.green}Você ganhou ${quantidade}{c.x}.')
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print()
        print(f'{c.bold_white_blue}=== {self} iniciou uma batalha com {pessoa} ==={c.x}')
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
                    print(textwrap.dedent(f'''
                        {c.bold_white_red} ==== {self} ganhou a batalha ==== {c.x} \n'''))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                if pokemon_inimigo.atacar(pokemon):  # Vitória inimiga
                    print(textwrap.dedent(f'''
                        {c.bold_white_red} ==== {pessoa} ganhou a batalha ==== {c.x} \n'''))
                    break
        else:
            print('Essa batalha não pode ocorrer...')


class Player(Pessoa):  # Player = subtipo da pessoa
    tipo = 'player'
    
    def capturar(self, pokemon):  # now it is working :)
        self.pokemons.append(pokemon)
        print()
        print(f'{c.green}{self} capturou {pokemon}!{c.x}')
        print()
        
        self.verificar_conquistas()

    def verificar_conquistas(self):
        if len(self.pokemons) == 5:
            print(f'{c.bold_white_blue}🏆 Conquista desbloqueada: Colecionador Inicial - 5 Pokémons capturados!{c.x}')
        if len(self.pokemons) == 10:
            print(f'{c.bold_white_blue}🏆 Conquista desbloqueada: Colecionador Mediano - 10 Pokémons capturados!{c.x}')
        if len(self.pokemons) == 20:
            print(f'{c.bold_white_blue}🏆 Conquista desbloqueada: Colecionador Master - 20 Pokémons capturados!{c.x}')
        if len(self.pokemons) == 30:
            print(f'{c.bold_white_blue}🏆 Conquista desbloqueada: Colecionador Expert - 30 Pokémons capturados!{c.x}')
        if len(self.pokemons) == 40:
            print(f'{c.bold_white_blue}🏆 Conquista desbloqueada: Última conquista da classe Colecionador - 40 Pokémons capturados! - Nível Supremo atingido. {c.x}')
        

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                try:
                    escolha = int(input('Escolha seu pokemon: '))
                    pokemon_escolhido = self.pokemons[escolha-1]
                    print()
                    print(f'{c.bold_green}{pokemon_escolhido}, eu escolho você!{c.x}')
                    print(textwrap.dedent(f'''
                        {c.bold_white_blue}================= ARENA ================={c.x} \n'''))
                    return pokemon_escolhido
                except:
                    print(f'{c.italic_red}Escolha inválida{c.x}')
        else:
            print('\033[3;31mERRO: Esse jogador não possui nenhum pokemon{c.x}}')

    def explorar(self):
        # switch instead if?
        if random.random() <= 0.3:  # 30% de chance de isso acontecer
            pokemon = random.choice(POKEMONS)
            print()
            sleep(1)
            print(f'{c.green}Um Pokémon selvagem apareceu: {pokemon}.{c.x}')
            print()
            sleep(1)

            escolha = str(input('Deseja capturar o Pokémon? [S/N] ')).upper().strip()
            if escolha == 'S':
                if random.random() >= 0.5:
                    self.capturar(pokemon) 
                    self.mostrar_pokemons()
                    
                else:
                    sleep(1)
                    print(f'{c.red}Oh não! {pokemon} fugiu. Boa sorte na próxima...{c.x}')
            else:
                sleep(1)
                print('Ok, boa viagem!')
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
            for i in range(random.randint(1, 6)):  # Escolha uma qnt aleatória de pokémons aleatórios
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemons_aleatorios)  # Chama o init classe pai (Pessoa)

        else:
            super().__init__(nome=nome, pokemons=pokemons)
