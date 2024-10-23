import unittest
import cap

class TestCap(unittest.TestCase):

    def test_ine_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')


    def test_multiple_words(self):
        text = 'aniket python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Aniket Python')
if __name__=='__main__':
    unittest.main()
