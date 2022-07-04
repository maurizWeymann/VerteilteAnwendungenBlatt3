# Unit-Test Demo

import unittest
import main as testmodul


VALUE_1 = 10.0
VALUE_2 = 5.0

class Test10Demo(unittest.TestCase):
    def test_add(self):
        """
        Test add function from testmodul
        """
        self.assertAlmostEqual(testmodul.add(VALUE_1, VALUE_2), 15.0)

    def test_mul(self):
        """
        Test mul function from testmodul
        """
        self.assertAlmostEqual(testmodul.mul(VALUE_1, VALUE_2), 50.0)

    def test_sub(self):
        """
        Test sub function from testmodul
        """
        self.assertAlmostEqual(testmodul.sub(VALUE_1, VALUE_2), 5.0)

if __name__ == '__main__':
    unittest.main()