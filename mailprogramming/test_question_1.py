import unittest
from mailprogramming import question_1


class Question1TestCase(unittest.TestCase):

    def test_do_1(self):
        input = [-1, 3, -1, 5]
        self.assertEqual(7, question_1.do(input))

    def test_do_2(self):
        input = [-5, -3, -1]
        self.assertEqual(-1, question_1.do(input))

    def test_do_3(self):
        input = [2, 4, -2, -3, 8]
        self.assertEqual(9, question_1.do(input))

    def test_do_4(self):
        input = [-100, -80, 200, -500, 9000]
        self.assertEqual(9000, question_1.do(input))


if __name__ == '__main__':
    unittest.main()
