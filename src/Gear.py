from math import cos


class Gear:
    def __init__(self, number_of_teeth, normal_module, helix_angle, helix_direction, left_flank, right_flank):
        self.__number_of_teeth = number_of_teeth
        self.__normal_module = normal_module
        self.__helix_angle = helix_angle
        self.__helix_direction = helix_direction
        self.__left_flank = left_flank
        self.__right_flank = right_flank
        self.__pitch_diameter = self.calc_pitch_diameter()

    def __get_number_of_teeth(self):
        return self.__number_of_teeth

    def __get_normal_module(self):
        return self.__normal_module

    def __get_helix_angle(self):
        return self.__helix_angle

    def __get_helix_direction(self):
        return self.__helix_direction

    def __get_left_flank(self):
        return self.__left_flank

    def __get_right_flank(self):
        return self.__right_flank

    def calc_pitch_diameter(self):
        return self.normal_module * self.number_of_teeth / cos(self.helix_angle)

    number_of_teeth = property(__get_number_of_teeth)
    normal_module = property(__get_normal_module)
    helix_angle = property(__get_helix_angle)
    helix_direction = property(__get_helix_direction)
    left_flank = property(__get_left_flank)
    right_flank = property(__get_right_flank)
