'''Tests for translator module'''
import unittest
from machinetranslation.translator import english_to_french, french_to_english


class TestTranslation(unittest.TestCase):
    ''' Simple tests of Translator API '''

    def test_english_to_french(self):
        ''' Basic en->fr '''
        en_text = 'Hello'
        fr_text = 'Bonjour'
        self.assertEqual(english_to_french(en_text), fr_text)

    def test_french_to_english(self):
        ''' Basic fr->en '''
        en_text = 'Hello'
        fr_text = 'Bonjour'
        self.assertEqual(french_to_english(fr_text), en_text)


if __name__ == '__main__':
    unittest.main()
