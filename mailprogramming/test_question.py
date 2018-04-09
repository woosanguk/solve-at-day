import unittest
from mailprogramming import question_1
from mailprogramming import question_2
from mailprogramming import question_4


class Question1TestCase(unittest.TestCase):

    def test_question_1(self):
        self.assertEqual(7, question_1.do([-1, 3, -1, 5]))
        self.assertEqual(-1, question_1.do([-5, -3, -1]))
        self.assertEqual(9, question_1.do([2, 4, -2, -3, 8]))
        self.assertEqual(9000, question_1.do([-100, -80, 200, -500, 9000]))

    def test_question_2(self):
        self.assertEqual(10, question_2.do(12))

    def test_question_4(self):
        self.assertFalse(question_4.do(12345))
        self.assertFalse(question_4.do(-101))
        self.assertTrue(question_4.do(11111))
        self.assertTrue(question_4.do(12421))






if __name__ == '__main__':
    unittest.main()
