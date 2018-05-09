from time import sleep
from sys import stdout
import random




class Represent:

    @staticmethod
    def progress_bar(msg='', wait=1, repeat=3):
        print(msg, end=' ')
        for i in range(repeat):
            stdout.write(".")
            stdout.flush()
            sleep(wait)
        print()


class Game:

    @staticmethod
    def set_game_mode():
        while True:
            print('Select game mode:\n1. U vs. C\n2. U vs. U\n3. C vs. C\n')
            modes = {'1': (User, Computer),
                     '2': (User, User),
                     '3': (Computer, Computer)}
            game_mode = modes.get(input('Your choice: '))
            if game_mode is not None:
                return game_mode
            print('Incorect answer. Try again!')

    @staticmethod
    def set_army_size():
        while True:
            try:
                army_size = int(input('Max size of army: '))
            except ValueError:
                print('Incorect answer! Value must be an integer number')
                continue
            if army_size > 0:
                return army_size
            print('Incorect answer! Value must be a number greater then zero')


class Player:

    counter = 1
    reserved_names = []

    def __init__(self):
        self.identify = 'Player {}'.format(Player.counter)
        self.army = []

        # load_msg = 'Preparing {}'.format(self.identify)
        Player.counter += 1

        # Represent.progress_bar(msg=load_msg, repeat=5)

    def set_player_name(self, name):
        Player.reserved_names.append(name)
        self.name = name


class Computer(Player):

    def set_player_name(self):
        while True:
            name = random.choice(NICKNAMES)
            if name not in self.reserved_names:
                super().set_player_name(name)
                break

    def create_army(self, empty_slots, complexity=1):
        army = []
        empty_slots *= complexity
        for squad in SQUADS[:-1]:
            q_pers = random.randint(0, empty_slots)
            army.append((squad, q_pers))
            empty_slots -= q_pers
        if empty_slots > 0:
            army.append((SQUADS[-1], empty_slots))
        self.army = army


class User(Player):

    def set_player_name(self):
        while True:
            name = input('{}, select your name: '.format(self.identify))
            if name not in self.reserved_names:
                super().set_player_name(name)
                break
            print('This name already exists! Select another.')


class Warior:
    pass


class Archer:
    pass


class Mage:
    pass


def main():
    players = Game.set_game_mode()
    army_size = Game.set_army_size()

    player1 = players[0]()
    player1.set_player_name()
    player1.create_army(army_size)

    player2 = players[1]()
    player2.set_player_name()
    player2.create_army(army_size)

    print(player1.name)
    print(player1.army)

    print(player2.name)
    print(player2.army)


NICKNAMES = ['Mammoth', 'Lobster', 'Highlander', 'Mastodon', 'Slug',
             'Prawn', 'Canine', 'Spider', 'Taz', 'Ratman', 'Hammerhead',
             'Sabre-Tooth', 'Sabertooth', 'Gecko', 'Bear', 'Zee-donk',
             'Dragon', 'Yak', 'Viper', 'Vulture', 'Thunderbird', 'Fish',
             'Dino', 'Froggy', 'Jackal', 'T-Rex', 'Wasp', 'Megalodon',
             'Raptor', 'Snake', 'Hound Dog', 'Bandicoot', 'Wildcat',
             'Bulldog', 'Gator', 'Husky', 'Catfish', 'Trunk', 'Dingo',
             'Bird', 'Bull', 'Longhorn']

SQUADS = [Warior, Archer, Mage]


if __name__ == '__main__':
    main()
