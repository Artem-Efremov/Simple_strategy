from time import sleep
from sys import stdout


class Represent:

    @staticmethod
    def progress_bar(msg='', wait=1, repeat=3):
        print(msg, end=' ')
        for i in range(repeat):
            stdout.write(".")
            stdout.flush()
            sleep(wait)
        print()
