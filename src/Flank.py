import numpy


class Flank:
    def __init__(self, side, pressure_angle, beta):
        self.__side = side
        self.__normal_pressure_angle = pressure_angle
        self.__transverse_pressure_angle = calc_transverse_pressure_angle(pressure_angle, beta)

    def __get_side(self):
        return self.__side

    def __get_normal_pressure_angle(self):
        return self.__normal_pressure_angle

    def __get_transverse_pressure_angle(self):
        return self.__transverse_pressure_angle

    side = property(__get_side)
    normal_pressure_angle = property(__get_normal_pressure_angle)
    transverse_pressure_angle = property(__get_transverse_pressure_angle)


def calc_transverse_pressure_angle(alpha_n, beta):
    return numpy.arctan(numpy.tan(alpha_n) / numpy.cos(beta))
