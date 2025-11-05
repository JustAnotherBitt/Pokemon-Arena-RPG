from time import sleep
import colors as c
import textwrap
from pokemon import * # Importa todas as classes

nameS = ['AbyssWanderer', 'ShadowReaper', 'CrypticPhantom',
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

    def __init__(self, name=None, pokemons=None, money=100):
        pokemons = [] if pokemons is None else pokemons
        self.name = name or random.choice(nameS)
        self.pokemons = pokemons
        self.money = money
        self.conquistas = []
        self.numero_conquistas = 0

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'name': self.name,
            'money': self.money,
            'pokemons': [p.to_dict() for p in self.pokemons],
            'tipo': self.tipo,
            'conquistas': self.conquistas,
            'numero_conquistas': self.numero_conquistas
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(data['name'])
        player.money = data['money']
        player.pokemons = [Pokemon.from_dict(p) for p in data['pokemons']]
        player.conquistas = data.get('conquistas', [])
        player.numero_conquistas = data.get('numero_conquistas', len(player.conquistas))
        return player

    def mostrar_pokemons(self):
        if self.pokemons:
            sleep(0.5)
            print(f'{c.yellow}\nPokémons de {self}:{c.x}')
            for index, pokemon in enumerate(self.pokemons, start=1):
                print(f'{index} - {pokemon}')
            sleep(0.5)
        else:
            print(f'{self} não possui nenhum pokemon.')
            sleep(0.5)

    def mostrar_conquistas(self):
        sleep(0.5)
        if self.conquistas:
            print(f'{c.yellow}\nConquistas de {self}:{c.x}')
            for conquista in self.conquistas:
                print(f' - {conquista}')
            sleep(0.5)
        else:
            print("\nNenhuma conquista desbloqueada ainda.")

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{c.blue}{self} escolheu {pokemon_escolhido}.{c.x}')
            return pokemon_escolhido
        else:
            print(f'\033[3;31mERRO: Esse jogador não possui nenhum Pokémon.{c.x}')

    def mostrar_dinheiro(self):  # Exibe mas o valor é self.money
        sleep(0.5)
        print(f'\nVocê possui {c.green}${self.money}{c.x} em sua conta.')

    def ganhar_dinheiro(self, quantidade):
        self.money += quantidade
        print(f'{c.green}Você ganhou ${quantidade}{c.x}.')
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print(f'\n{c.bold_white_blue}=== {self} iniciou uma batalha com {pessoa} ==={c.x}')
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

                if pokemon_inimigo.atacar(pokemon):
                    print(textwrap.dedent(f'''
                        {c.bold_white_red} ==== {pessoa} ganhou a batalha ==== {c.x} \n'''))
                    break
        else:
            print('Essa batalha não pode ocorrer...')



class Player(Pessoa):
    tipo = 'player'
    
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'\n{c.green}{self} capturou {pokemon}!{c.x}\n')
        self.verificar_conquistas()

    def verificar_conquistas(self):
        total = len(self.pokemons)
        conquistas = {
            2: "test",
            3: "test2",
            4: "test3",
            5: "Colecionador Inicial - 5 Pokémons capturados!",
            10: "Colecionador Mediano - 10 Pokémons capturados!",
            20: "Colecionador Master - 20 Pokémons capturados!",
            30: "Colecionador Expert - 30 Pokémons capturados!",
            40: "Última conquista da classe Colecionador - 40 Pokémons capturados! - Nível Supremo atingido."
        }
                                            
        if total in conquistas:
            conquista_nome = conquistas[total]
            print(f'{c.bold_white_blue}🏆 Conquista desbloqueada: {conquistas[total]}{c.x}')
            self.conquistas.append(conquista_nome)
            
        self.numero_conquistas = len(self.conquistas)
                
                
    def escolher_pokemon(self):
        self.mostrar_pokemons()
        if self.pokemons:
            while True:
                try:
                    escolha = int(input('Escolha seu Pokémon: '))
                    pokemon_escolhido = self.pokemons[escolha-1]
                    print()
                    print(f'{c.bold_green}{pokemon_escolhido}, eu escolho você!{c.x}')
                    print(textwrap.dedent(f'''
                        {c.bold_white_blue}================= ARENA ================={c.x} \n'''))
                    return pokemon_escolhido
                except:
                    print(f'{c.italic_red}Escolha inválida{c.x}')
        else:
            print(f'{c.bold_red}ERRO: Esse jogador não possui nenhum Pokémon{c.x}')

    def explorar(self):
        print(f'\n{c.bold_blue}=== {self} está explorando... ==={c.x}')
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            sleep(1)
            print(f'{c.green}\nUm Pokémon selvagem apareceu: {pokemon}.{c.x}\n')
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
                print('Você devia responder com apenas S ou N... Mas tudo bem, o Pokémon fugiu.')
        else:
            sleep(2)
            print(f'{c.yellow}\nEssa exploração não deu em nada...{c.x}\n')
            sleep(1)

    def to_dict(self):
        return {
            'name': self.name,
            'money': self.money,
            'pokemons': [p.to_dict() for p in self.pokemons],
            'tipo': self.tipo,
            'conquistas': self.conquistas,
            'numero_conquistas': self.numero_conquistas
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(data['name'])
        player.money = data['money']
        player.pokemons = [Pokemon.from_dict(p) for p in data['pokemons']]
        player.conquistas = data.get('conquistas', [])
        player.numero_conquistas = data.get('numero_conquistas', len(player.conquistas))
        return player


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, name=None, pokemons=None):
        if not pokemons:  # Se não tiver pokémons
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):  # Escolha uma qnt aleatória de pokémons aleatórios
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(name=name, pokemons=pokemons_aleatorios)  # Chama o init classe pai (Pessoa)

        else:
            super().__init__(name=name, pokemons=pokemons)
