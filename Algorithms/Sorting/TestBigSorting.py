import unittest

from Algorithms.Sorting.BigSorting import solve


class BigSortingTestCase(unittest.TestCase):
    def test_problem(self):
        self.assertEqual([1, 3, 3, 5, 10, 31415926535897932384626433832795],
                         solve(6, [31415926535897932384626433832795, 1, 3, 10, 3, 5]))
        self.assertEqual(['1', '3', '3', '5', '10', '31415926535897932384626433832795'],
                         solve(6, ['31415926535897932384626433832795', '1', '3', '10', '3', '5']))