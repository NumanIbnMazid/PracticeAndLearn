
import unittest
import cap

class CapTest(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_func(text)
        self.assertEqual(result, 'Python')

    def test_two_word(self):
        text = 'numan python'
        result = cap.cap_func(text)
        self.assertEqual(result, 'Numan Python')


if __name__ == '__main__':
    unittest.main()