from players import User, Computer
from representation import Represent
from check import Checker


class Game:

    def set_game_mode(self):
        modes = ((User, Computer), (User, User), (Computer, Computer))
        pattern = '{i}. {p[0].__name__} vs. {p[1].__name__}'
        while True:
            print('Select game mode:')
            for i, players in enumerate(modes, 1):
                print(pattern.format(i=i, p=players))
            answer = input('\nYour choice: ')
            if (Checker.check_str_loks_like_int_num(answer) and
                   Checker.check_number_in_range(int(answer), end=len(modes))):
                self.gamemode = modes[int(answer) - 1]
                break

    def set_army_size(self):
        while True:
            army_size = input('Max size of army: ')
            if (Checker.check_str_loks_like_int_num(army_size) and
                    Checker.check_number_in_range(int(army_size), 0)):
                self.army_size = int(army_size)
                break

    @Represent.battle_decorator
    def battle(self, player1, player2):
        lap = 1
        while True:
            p1_squad = player1.get_next_squad()
            p2_squad = player2.get_next_squad()
            if not p1_squad or not p2_squad:
                break
            p1_squad.fight(p2_squad, player1, player2, lap)
            lap += 1


def main():
    game = Game()
    game.set_game_mode()
    game.set_army_size()

    players = []
    for i in range(2):
        player = game.gamemode[i]()
        player.set_player_name()
        player.create_army(game.army_size)
        players.append(player)

    game.battle(*players)


if __name__ == '__main__':
    main()
    input('Press any key to exit ')
