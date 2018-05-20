from math import floor
from representation import Represent


class Units:

    def __init__(self, squad_size):
        self.squad_size = squad_size
        self.casualties = 0

    def get_coeficient(self, other):
        table = {
            (Warriors, Archers): (2, 0.5),
            (Archers, Mages): (2, 0.5),
            (Mages, Warriors): (2, 0.5),
            (Archers, Warriors): (0.5, 2),
            (Mages, Archers): (0.5, 2),
            (Warriors, Mages): (0.5, 2),
            (Warriors, Warriors): (1, 1),
            (Archers, Archers): (1, 1),
            (Mages, Mages): (1, 1),
        }
        return table.get((type(self), type(other)))

    @Represent.fight_decorator
    def fight(self, other):
        start_size = (self.squad_size, other.squad_size)

        coef1, coef2 = self.get_coeficient(other)
        force1 = floor(coef1 * self.squad_size)
        force2 = floor(coef2 * other.squad_size)

        self.casualties += min(self.squad_size, force2)
        other.casualties += min(other.squad_size, force1)

        self.squad_size = max(0, self.squad_size - force2)
        other.squad_size = max(0, other.squad_size - force1)
        return {'casualties': (self.casualties, other.casualties),
                'start_size': start_size}


class Warriors(Units):
    pass


class Archers(Units):
    pass


class Mages(Units):
    pass


SQUADS = (Warriors, Archers, Mages)
