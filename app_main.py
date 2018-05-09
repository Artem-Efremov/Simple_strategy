from players import User, Computer
from representation import Represent
from check import Checker


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
            value = input('Max size of army: ')
            if not Checker.check_str_loks_like_int_num(value):
                continue
            army_size = int(value)
            if army_size > 0:
                return army_size
            print('Incorect answer! Value must be a number greater then zero')

    @staticmethod
    def battle(player1, player2):
        Represent.progress_bar('Loading', 0.5, 20)


def main():
    players = Game.set_game_mode()
    army_size = Game.set_army_size()

    player1 = players[0]()
    player1.set_player_name()
    player1.create_army(army_size)

    player2 = players[1]()
    player2.set_player_name()
    player2.create_army(army_size)

    Game.battle(player1, player2)

    print(player1.name)

    for squad in player1.army:
        print(squad.squad_size)

    print(player2.name)
    for squad in player2.army:
        print(squad.squad_size)


if __name__ == '__main__':
    main()
