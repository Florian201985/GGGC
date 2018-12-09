import numpy

from src import Gear


class Flank:
    def __init__(self, side, pressure_angle, beta, mn, z):
        self.__side = side
        self.__normal_pressure_angle = pressure_angle
        self.__transverse_pressure_angle = calc_transverse_pressure_angle(pressure_angle, beta)
        self.__base_circle_diameter = calc_base_circle_diameter(self.__transverse_pressure_angle, mn, beta, z)

    def __get_side(self):
        return self.__side

    def __get_normal_pressure_angle(self):
        return self.__normal_pressure_angle

    def __get_transverse_pressure_angle(self):
        return self.__transverse_pressure_angle

    def __get_base_circle_diameter(self):
        return self.__base_circle_diameter

    side = property(__get_side)
    normal_pressure_angle = property(__get_normal_pressure_angle)
    transverse_pressure_angle = property(__get_transverse_pressure_angle)
    base_circle_diameter = property(__get_base_circle_diameter)


def calc_transverse_pressure_angle(alpha_n, beta):
    return numpy.arctan(numpy.tan(alpha_n) / numpy.cos(beta))


def calc_base_circle_diameter(alpha_t, mn, beta, z):
    d = Gear.calc_pitch_diameter(mn, z, beta)
    return d * numpy.cos(alpha_t)