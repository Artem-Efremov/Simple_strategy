from players import User, Computer
from representation import Represent
from check import Checker
from time import sleep


class Game:

    @staticmethod
    def set_game_mode():
        modes = ((User, Computer), (User, User), (Computer, Computer))
        pattern = '{i}. {p[0].__name__} vs. {p[1].__name__}'
        while True:
            print('Select game mode:')
            for i, players in enumerate(modes, 1):
                print(pattern.format(i=i, p=players))
            answer = input('\nYour choice: ')
            if (Checker.check_str_loks_like_int_num(answer) and
                   Checker.check_number_in_range(int(answer), end=len(modes))):
                return modes[int(answer) - 1]

    @staticmethod
    def set_army_size():
        while True:
            army_size = input('Max size of army: ')
            if (Checker.check_str_loks_like_int_num(army_size) and
                    Checker.check_number_in_range(int(army_size), 0)):
                return int(army_size)

    @staticmethod
    def battle(player1, player2):
        print('Start battle')
        lap = 1
        while True:
            p1_squad = player1.get_next_squad()
            p2_squad = player2.get_next_squad()
            if not p1_squad or not p2_squad:
                break

            print('\nRound {}\n'.format(lap))
            print(player1.name + '\'s', p1_squad.__class__.__name__, p1_squad.squad_size)
            print('vs')
            print(player2.name + '\'s', p2_squad.__class__.__name__, p2_squad.squad_size)
            p1_squad.fight(p2_squad)
            print('Result of Round {}:'.format(lap))
            print('{} casualties: {}'.format(player1.name, p1_squad.casualties))
            print('{} casualties: {}'.format(player2.name, p2_squad.casualties))
            lap += 1
            sleep(3)
        print(player1.name, 'casualties:')
        for squad in player1.army:
            if squad.casualties > 0:
                print(squad.__class__.__name__, squad.casualties)
        print(player2.name, 'casualties:')
        for squad in player2.army:
            if squad.casualties > 0:
                print(squad.__class__.__name__, squad.casualties)

    @staticmethod
    def result_of_battle(player1, player2):
        return player1.is_survived() - player2.is_survived()


def main():
    gamemode = Game.set_game_mode()
    army_size = Game.set_army_size()

    players = []
    for i in range(2):
        # Represent.progress_bar(msg='Preparing Player {}'.format(i+1), repeat=5)
        player = gamemode[i]()
        player.set_player_name()
        player.create_army(army_size)
        players.append(player)

    # Represent.progress_bar(msg='Loading', repeat=15)
    Game.battle(*players)
    a = Game.result_of_battle(*players)
    print((players[0].name + ' WIN!',
           'Draw',
           players[1].name + ' WIN!')[a + 1])


if __name__ == '__main__':
    main()
    input('Press any key to exit ')
