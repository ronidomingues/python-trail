import unittest
from exercises.armstrong_number import ArmstrongNumber

class TestArmstrongNumber(unittest.TestCase):
    def test_is_armstrong_number_true(self):
        self.assertTrue(ArmstrongNumber(153).is_armstrong_number())
        self.assertTrue(ArmstrongNumber(370).is_armstrong_number())
        self.assertTrue(ArmstrongNumber(371).is_armstrong_number())
        self.assertTrue(ArmstrongNumber(9474).is_armstrong_number())
    def test_is_armstrong_number_false(self):
        self.assertFalse(ArmstrongNumber(152).is_armstrong_number())
        self.assertFalse(ArmstrongNumber(372).is_armstrong_number())
        self.assertFalse(ArmstrongNumber(9475).is_armstrong_number())
    def test_single_digit(self):
        # Todo número de um dígito é sempre um Número de Armstrong, pois ele é igual ao seu proprio valor elevado ao número de dígitos.
        for i in range(10):
            self.assertTrue(ArmstrongNumber(i).is_armstrong_number())
if __name__ == "__main__":
    unittest.main()