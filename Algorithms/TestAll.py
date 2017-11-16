import unittest

from Algorithms.Implementation.TestImplementation import ImplementationTestCase
from Algorithms.Search.TestSearch import SearchTestCase
from Algorithms.Sorting.TestSorting import SortingTestCase
from Algorithms.Strings.TestStrings import StringsTestCase


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(StringsTestCase())
    test_suite.addTest(SortingTestCase())
    test_suite.addTest(SearchTestCase())
    test_suite.addTest(ImplementationTestCase())
    return test_suite


if __name__ == "__main__":
    unittest.main()
