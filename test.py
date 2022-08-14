import unittest
import iqv_calculator


class MyTestCase(unittest.TestCase):
    def test_with_ratio(self):

        test_1 = [0.6, 0.3, 32, 34, 23, 10.1]
        test_var = iqv_calculator.get_iqv(test_1, True)
        self.assertEqual(0.8626248, test_var)

    def test_without_ratio(self):
        test_2 = [6, 3, 320, 340, 230, 101]
        test_var = iqv_calculator.get_iqv(test_2, False)
        self.assertEqual(0.8626248, test_var)


if __name__ == "__main__":
    unittest.main()
