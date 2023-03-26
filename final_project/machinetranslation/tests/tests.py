
import unittest as unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    '''
    Test for translator
    '''
    def test_english_to_french(self):
        #self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english(self):
         #self.assertEqual(french_to_english(None), None)
         self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()