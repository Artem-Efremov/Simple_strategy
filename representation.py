from time import sleep
from sys import stdout


class Represent:

    @staticmethod
    def fight_decorator(decorated_func):
        def wrapper(self, other, player1, player2, lap):
            Represent.start_round(self, other, player1, player2, lap)
            Represent.progress_bar(msg='\nFighting', repeat=5, wait_after=2)
            result = decorated_func(self, other)
            Represent.print_out('\nResult of Round {}:'.format(lap), wait_after=1)
            Represent.print_out('{}\'s casualties: {} {}'.format(player1.name,
                    self.__class__.__name__, self.casualties), wait_after=0)
            Represent.print_out('{}\'s casualties: {} {}'.format(player2.name,
                    other.__class__.__name__, other.casualties), wait_after=2)
            return result
        return wrapper

    @staticmethod
    def battle_decorator(decorated_func):
        def wrapper(self, player1, player2):
            Represent.progress_bar(msg='Loading', repeat=15, wait_after=1)
            Represent.print_out('\nStart battle', wait_after=1)
            decorated_func(self, player1, player2)
            sleep(1)
            Represent.game_result(player1, player2)
        return wrapper

    @staticmethod
    def progress_bar(msg='', wait=0.5, repeat=3, wait_after=0):
        print(msg, end=' ')
        for i in range(repeat):
            stdout.write(".")
            stdout.flush()
            sleep(wait)
        Represent.print_out(wait_after=wait_after)

    @staticmethod
    def game_result(*players):
        result = players[0].is_survived() - players[1].is_survived()
        variants = (players[0].name + ' WIN!', 'Draw', players[1].name + ' WIN!')
        Represent.print_out('Result of battle:\n', wait_after=1)
        Represent.print_out(variants[result + 1], end='\n\n', wait_after=2)
        for i in range(2):
            Represent.print_out(players[i].name, 'casualties:', wait_after=1)
            for squad in players[i].army:
                if squad.casualties > 0:
                    print(squad.__class__.__name__, squad.casualties)
            Represent.print_out(wait_after=1)

    @staticmethod
    def start_round(p1_squad, p2_squad, player1, player2, lap):
        Represent.print_out('\nRound {}\n'.format(lap), wait_after=2)
        print(player1.name + '\'s', p1_squad.__class__.__name__, p1_squad.squad_size)
        print('vs')
        print(player2.name + '\'s', p2_squad.__class__.__name__, p2_squad.squad_size)
        Represent.print_out(wait_after=1)

    @staticmethod
    def print_out(*args, wait_after=0, **kwargs):
        print(*args, **kwargs)
        sleep(wait_after)
