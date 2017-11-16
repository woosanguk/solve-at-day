import unittest

from Algorithms.Implementation.DivisibleSumPairs import divisible_sum_pairs_solve
from Algorithms.Implementation.Kangaroo import kangaroo_solve as kangaroo_solve


class SearchTestCase(unittest.TestCase):

    def test_kangaroo(self):
        self.assertEqual('YES', kangaroo_solve(0, 3, 4, 2))
        self.assertEqual('NO', kangaroo_solve(0, 2, 5, 3))

    def test_divisible_sum_pairs(self):
        self.assertEqual(5, divisible_sum_pairs_solve(6, 3, [1, 3, 2, 6, 1, 2]))


if __name__ == '__main__':
    unittest.main()
