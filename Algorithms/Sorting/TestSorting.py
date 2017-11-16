import unittest

from Algorithms.Sorting.BigSorting import big_sorting_solve
from Algorithms.Sorting.CorrectnessAndTheLoopInvariant import correctness_and_the_loop_invariant_solve


class SortingTestCase(unittest.TestCase):
    def test_big_sorting(self):
        self.assertEqual([1, 3, 3, 5, 10, 31415926535897932384626433832795],
                         big_sorting_solve(6, [31415926535897932384626433832795, 1, 3, 10, 3, 5]))
        self.assertEqual(['1', '3', '3', '5', '10', '31415926535897932384626433832795'],
                         big_sorting_solve(6, ['31415926535897932384626433832795', '1', '3', '10', '3', '5']))

    def test_correctness_and_the_loop_invariant(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], correctness_and_the_loop_invariant_solve([4, 1, 3, 5, 6, 2]))
