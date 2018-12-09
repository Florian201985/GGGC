import unittest

from src import Import


class ImportTest(unittest.TestCase):

    def test_extract_value_from_line_value1(self):
        line = "*wxyz 10.0     ** test line"
        exp_value = "10.0"
        actual = Import.extract_value_from_line(line)
        self.assertEqual(exp_value, actual)

    def test_extract_value_from_line_value2(self):
        line = "*wxyz 11.0     ** test line"
        exp_value = "11.0"
        actual = Import.extract_value_from_line(line)
        self.assertEqual(exp_value, actual)
