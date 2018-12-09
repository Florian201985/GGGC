from math import cos

import numpy

from src import Parameter


def calc_pitch_diameter(mn, z, beta):
    return mn * abs(z) / cos(beta)


def calc_transverse_module(mn, beta):
    return mn / numpy.cos(beta)


def calc_axial_module(mn, beta):
    if abs(beta) <= Parameter.Precision.eps_normal:
        return float('nan')
    else:
        return mn / numpy.sin(abs(beta))


class Gear:
    def __init__(self, number_of_teeth, normal_module, helix_angle, left_flank, right_flank):
        if number_of_teeth > 0:
            self.__internal_external = Parameter.InternalExternal.EXTERNAL
        else:
            self.__internal_external = Parameter.InternalExternal.INTERNAL
        self.__number_of_teeth = abs(number_of_teeth)
        self.__normal_module = normal_module
        if helix_angle > 0:
            self.__helix_direction = Parameter.DirectionHelixAngle.RIGHT
        else:
            self.__helix_direction = Parameter.DirectionHelixAngle.LEFT
        self.__helix_angle = abs(helix_angle)
        self.__left_flank = left_flank
        self.__right_flank = right_flank
        self.__pitch_diameter = calc_pitch_diameter(self.normal_module, self.number_of_teeth, self.helix_angle)
        self.__transverse_module = calc_transverse_module(self.__normal_module, self.__helix_angle)
        self.__axial_module = calc_axial_module(self.__normal_module, self.__helix_angle)

    def __get_number_of_teeth(self):
        return self.__number_of_teeth

    def __get_internal_external(self):
        return self.__internal_external

    def __get_normal_module(self):
        return self.__normal_module

    def __get_transverse_module(self):
        return self.__transverse_module

    def __get_axial_module(self):
        return self.__axial_module

    def __get_helix_angle(self):
        return self.__helix_angle

    def __get_helix_direction(self):
        return self.__helix_direction

    def __get_left_flank(self):
        return self.__left_flank

    def __get_right_flank(self):
        return self.__right_flank

    def __get_pitch_diameter(self):
        return self.__pitch_diameter

    number_of_teeth = property(__get_number_of_teeth)
    internal_external = property(__get_internal_external)
    normal_module = property(__get_normal_module)
    helix_angle = property(__get_helix_angle)
    helix_direction = property(__get_helix_direction)
    left_flank = property(__get_left_flank)
    right_flank = property(__get_right_flank)
    pitch_diameter = property(__get_pitch_diameter)
    transverse_module = property(__get_transverse_module)
    axial_module = property(__get_axial_module)
