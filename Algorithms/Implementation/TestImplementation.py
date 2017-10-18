import unittest
from Algorithms.Implementation.Kangaroo import solve as kangaroo_solve


class SearchTestCase(unittest.TestCase):

    def test_kangaroo(self):
        self.assertEqual('YES', kangaroo_solve(0, 3, 4, 2))
        self.assertEqual('NO', kangaroo_solve(0, 2, 5, 3))

if __name__ == '__main__':
    unittest.main()
