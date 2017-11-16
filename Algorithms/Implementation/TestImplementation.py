import unittest

from Algorithms.Implementation.DayOfTheProgrammer import day_of_the_programmer_solve
from Algorithms.Implementation.DivisibleSumPairs import divisible_sum_pairs_solve
from Algorithms.Implementation.Kangaroo import kangaroo_solve as kangaroo_solve
from Algorithms.Implementation.MigratoryBirds import migratory_birds_solve


class ImplementationTestCase(unittest.TestCase):

    def test_kangaroo(self):
        self.assertEqual('YES', kangaroo_solve(0, 3, 4, 2))
        self.assertEqual('NO', kangaroo_solve(0, 2, 5, 3))

    def test_divisible_sum_pairs(self):
        self.assertEqual(5, divisible_sum_pairs_solve(6, 3, [1, 3, 2, 6, 1, 2]))

    def test_migratory_birds(self):
        self.assertEqual(4, migratory_birds_solve(6, [1, 4, 4, 4, 5, 3]))

    def test_day_of_the_programmer(self):
        self.assertEqual("13.09.2017", day_of_the_programmer_solve(2017))
        self.assertEqual("12.09.2016", day_of_the_programmer_solve(2016))
        self.assertEqual("26.09.1918", day_of_the_programmer_solve(1918))


if __name__ == '__main__':
    unittest.main()
