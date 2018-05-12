from math import ceil


class Units:

    def __init__(self, squad_size):
        self.squad_size = squad_size

    def get_coeficient(self, other):
        table = {
            (Wariors, Archers): (2, 0.5),
            (Archers, Mages): (2, 0.5),
            (Mages, Wariors): (2, 0.5),
            (Archers, Wariors): (0.5, 2),
            (Mages, Archers): (0.5, 2),
            (Wariors, Mages): (0.5, 2),
            (Wariors, Wariors): (1, 1),
            (Archers, Archers): (1, 1),
            (Mages, Mages): (1, 1),
        }
        return table.get((type(self), type(other)))

    def fight(self, other):
        coef1, coef2 = self.get_coeficient(other)
        force1 = ceil(coef1 * self.squad_size)
        print('squad1 power: {}'.format(force1))
        force2 = ceil(coef2 * other.squad_size)
        print('squad2 power: {}'.format(force1))

        self.casualties = min(self.squad_size, force2)
        print('squad1 casualties: {}'.format(self.casualties))
        other.casualties = min(other.squad_size, force1)
        print('squad2 casualties: {}'.format(other.casualties))

        self.squad_size = max(0, self.squad_size - force2)
        other.squad_size = max(0, other.squad_size - force1)


class Wariors(Units):
    pass


class Archers(Units):
    pass


class Mages(Units):
    pass


SQUADS = (Wariors, Archers, Mages)
