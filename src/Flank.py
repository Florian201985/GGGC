class Flank:
    def __init__(self, side, pressure_angle):
        self.__side = side
        self.__pressure_angle = pressure_angle

    def __get_side(self):
        return self.__side

    def __get_pressure_angle(self):
        return self.__pressure_angle

    side = property(__get_side)
    pressure_angle = property(__get_pressure_angle)

