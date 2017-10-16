import unittest

from Algorithms.Search.HackerLandRadioTransmitters import solve


class HackerLandRadioTransmittersTestCase(unittest.TestCase):
    def test_problem(self):
        self.assertEqual(1, solve(1, 2, [7]))
        self.assertEqual(2, solve(5, 1, [1, 2, 3, 4, 5]))
        self.assertEqual(3, solve(8, 2, [7, 2, 4, 6, 5, 9, 12, 11]))


if __name__ == '__main__':
    unittest.main()
