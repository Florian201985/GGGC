import unittest

from src import Converter, Flank


class FlankTest(unittest.TestCase):

    def test_calc_transverse_pressure_angle_spur_gear(self):
        beta = Converter.grad2rad(0.0)
        alpha_n = Converter.grad2rad(20.0)
        expected = Converter.grad2rad(20.0)
        actual = Flank.calc_transverse_pressure_angle(alpha_n, beta)
        self.assertAlmostEqual(expected, actual, 5)

    def test_calc_transverse_pressure_angle_helical_gear(self):
        beta = Converter.grad2rad(10.0)
        alpha_n = Converter.grad2rad(20.0)
        expected = Converter.grad2rad(20.283559)
        actual = Flank.calc_transverse_pressure_angle(alpha_n, beta)
        self.assertAlmostEqual(expected, actual, 5)
