import unittest
from spellchecker import check_spelling

class TestSpellChecker(unittest.TestCase):

    def test_no_errors(self):
        text = "мама мыла раму"
        result = check_spelling(text)
        self.assertEqual(len(result), 0)

    def test_empty_text(self):
        result = check_spelling("")
        self.assertEqual(result, [])

    def test_one_error_wrong_count(self):
        text = "мама мыла раму миррр"
        result = check_spelling(text)
        self.assertEqual(len(result), 2)

    def test_wrong_word_expected(self):
        text = "миррр"
        result = check_spelling(text)
        self.assertEqual(result[0]["word"], "мир")

    def test_too_many_suggestions(self):
        text = "миррр"
        result = check_spelling(text)
        self.assertEqual(len(result[0]["suggestions"]), 5)

    def test_wrong_position(self):
        text = "миррр"
        result = check_spelling(text)
        self.assertEqual(result[0]["position"], 999)

if __name__ == "__main__":
    unittest.main()