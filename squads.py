from math import floor
from representation import Represent


class Units:

    def __init__(self, squad_size):
        self.squad_size = squad_size
        self.total_casualties = 0
        self.last_round_casualties = 0

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
        coef1, coef2 = self.get_coeficient(other)
        force1 = floor(coef1 * self.squad_size)
        force2 = floor(coef2 * other.squad_size)

        self.last_round_casualties = min(self.squad_size, force2)
        other.last_round_casualties = min(other.squad_size, force1)

        self.total_casualties += self.last_round_casualties
        other.total_casualties += other.last_round_casualties

        self.squad_size -= self.last_round_casualties
        other.squad_size -= other.last_round_casualties


class Warriors(Units):
    pass


class Archers(Units):
    pass


class Mages(Units):
    pass


SQUADS = (Warriors, Archers, Mages)
