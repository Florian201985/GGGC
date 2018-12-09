import unittest

from src import Gear, Converter


class GearTest(unittest.TestCase):

    def test_calc_pitch_diameter_spur_gear(self):
        mn = 2.0
        z = 2
        beta = Converter.grad2rad(0.0)
        expected = 4.0
        actual = Gear.calc_pitch_diameter(mn, z, beta)
        self.assertAlmostEqual(expected, actual, 5)

    def test_calc_pitch_diameter_spur_inner_gear(self):
        mn = 2.0
        z = -2
        beta = Converter.grad2rad(0.0)
        expected = 4.0
        actual = Gear.calc_pitch_diameter(mn, z, beta)
        self.assertAlmostEqual(expected, actual, 5)

    def test_calc_pitch_diameter_positive_helical_gear(self):
        mn = 2.0
        z = 2
        beta = Converter.grad2rad(10.0)
        expected = 4.061706
        actual = Gear.calc_pitch_diameter(mn, z, beta)
        self.assertAlmostEqual(expected, actual, 5)

    def test_calc_pitch_diameter_negative_helical_gear(self):
        mn = 2.0
        z = 2
        beta = Converter.grad2rad(-10.0)
        expected = 4.061706
        actual = Gear.calc_pitch_diameter(mn, z, beta)
        self.assertAlmostEqual(expected, actual, 5)


