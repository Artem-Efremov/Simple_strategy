class Units:
    def __init__(self, squad_size):
        self.squad_size = squad_size


class Wariors(Units):
    pass


class Archers(Units):
    pass


class Mages(Units):
    pass


SQUADS = (Wariors, Archers, Mages)
