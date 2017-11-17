import unittest

from Algorithms.Strings.CamelCase import camel_case_solve
from Algorithms.Strings.TwoCharacters import two_characters_solve


class StringsTestCase(unittest.TestCase):
    def test_camel_case(self):
        self.assertEqual(5, camel_case_solve('saveChangesInTheEditor'))

    def two_characters_solve(self):
        self.assertEqual(5, two_characters_solve(10, "beabeefeab"))


if __name__ == '__main__':
    unittest.main()