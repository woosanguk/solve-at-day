import unittest

from Algorithms.Search.GridlandMetro import gridland_metro_solve
from Algorithms.Search.HackerLandRadioTransmitters import transmitters_solve
from Algorithms.Search.IntroToTutorialChallenges import ittc_solve


class SearchTestCase(unittest.TestCase):
    def test_hacker_land_radio_transmitters(self):
        self.assertEqual(1, transmitters_solve(1, 2, [7]))
        self.assertEqual(2, transmitters_solve(5, 1, [1, 2, 3, 4, 5]))
        self.assertEqual(3, transmitters_solve(8, 2, [7, 2, 4, 6, 5, 9, 12, 11]))

    def test_intro_to_tutorial_challenges(self):
        self.assertEqual(1, ittc_solve(4, 6, [1, 4, 5, 7, 9, 12]))

    def test_gridland_metro(self):
        self.assertEqual(9, gridland_metro_solve(4, 4, 3, [[2, 2, 3], [3, 1, 4], [4, 4, 4]]))


if __name__ == '__main__':
    unittest.main()
