from check import Checker
import squads
import random


class Player:

    counter = 1
    reserved_names = []

    def __init__(self):
        self.army = []
        self.identify = 'Player {}'.format(Player.counter)
        Player.counter += 1

    def set_player_name(self, name):
        self.name = name
        Player.reserved_names.append(name)

    def get_next_squad(self):
        for squad in self.army:
            if squad.squad_size != 0:
                return squad

    def is_survived(self):
        survivors = 0
        for squad in self.army:
            survivors += squad.squad_size
        return bool(survivors)


class Computer(Player):

    NICKNAMES = ['Bad Mr. Frosty', 'Kraken', 'Boomer', 'Lumberjack', 'Boss',
                 'Boomerang', 'Mammoth', 'Master', 'Mastadon', 'Budweiser',
                 'Bullseye', 'Meatball', 'Buster', 'Mooch', 'Butch', 'Buzz',
                 'Mr. President', 'Outlaw', 'Canine', 'Ratman', 'Renegade',
                 'Captian RedBeard', 'Champ', 'Sabertooth', 'Coma', 'Speed',
                 'Scratch', 'Crusher', 'Diesel', 'Sentinel', 'Frankenstein',
                 'Subwoofer', 'Doctor', 'Spike', 'Dreads',  'Thunderbird',
                 'Froggy', 'Tornado', 'General', 'Troubleshoot', 'Godzilla',
                 'Wizard', 'Hammerhead', 'Viper', 'King Kong', 'Hound Dog',
                 'Zodiac', 'Handy Man', 'Indominus', 'Vice', 'Wasp']

    def set_player_name(self):
        while True:
            name = random.choice(self.NICKNAMES)
            if name not in self.reserved_names:
                super().set_player_name(name)
                break

    def create_army(self, empty_slots, complexity=1):
        empty_slots *= complexity
        for squad in squads.SQUADS[:-1]:
            squad_size = random.randint(0, empty_slots)
            if squad_size != 0:
                self.army.append(squad(squad_size))
                empty_slots -= squad_size
        if empty_slots > 0:
            self.army.append(squads.SQUADS[-1](empty_slots))


class User(Player):

    def set_player_name(self):
        while True:
            name = input('{}, select your name: '.format(self.identify))
            if name not in self.reserved_names:
                super().set_player_name(name)
                break
            print('This name already exists! Select another.')

    def create_army(self, empty_slots):
        for squad in squads.SQUADS:
            while empty_slots > 0:
                value = input('Select quantity of the ' + squad.__name__ + ': ')
                if not Checker.check_str_loks_like_int_num(value):
                    continue
                squad_size = int(value)
                if 0 <= squad_size <= empty_slots:
                    if squad_size != 0:
                        self.army.append(squad(squad_size))
                        empty_slots -= squad_size
                    break
                print('Incorect answer! Value must be a number from range ' +
                      '[0, {}]'.format(empty_slots))
