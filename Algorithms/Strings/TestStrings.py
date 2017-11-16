import unittest

from Algorithms.Strings.CamelCase import camel_case_solve


class StringsTestCase(unittest.TestCase):
    def test_camel_case(self):
        self.assertEqual(5, camel_case_solve('saveChangesInTheEditor'))


if __name__ == '__main__':
    unittest.main()