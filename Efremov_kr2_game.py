class Game:

    def set_game_mode(self):
        while True:
            print('Select game mode:\n1. U vs. C\n2. U vs. U\n3. C vs. C\n')
            modes = {'1': (User, Computer),
                     '2': (User, User),
                     '3': (Computer, Computer)}
            game_mode = modes.get(input('Your choice: '))
            if game_mode is not None:
                return game_mode
            print('Incorect answer. Try again!')

    def set_army_size(self):
        while True:
            try:
                army_size = int(input('Max size of army: '))
            except ValueError:
                print('Incorect answer! Value must be an integer number')
            if army_size > 0:
                return army_size
            print('Incorect answer! Value must be a number greater then zero')


class Computer():
    pass


class User():
    pass


def main():
    game = Game()
    game_mode = game.set_game_mode()
    army_size = game.set_army_size()
    user1, user2 = game_mode[0](), game_mode[1]()


if __name__ == '__main__':
    main()
