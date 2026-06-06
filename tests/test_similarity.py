import unittest
from services.similarity import calculate_similarity

class TestSimilarity(unittest.TestCase):

    def test_identical_texts(self):
        text1 = "the quick brown fox jumped over the lazy dog"
        text2 = "the quick brown fox jumped over the lazy dog"
        result = calculate_similarity(text1, text2)
        self.assertEqual(result['similarity_score'], 100.0)

    def test_no_match(self):
        text1 = "abcdefghijklmnopqrstuvwxyz" * 5
        text2 = "zyxwvutsrqponmlkjihgfedcba" * 5
        result = calculate_similarity(text1, text2)
        self.assertEqual(result['similarity_score'], 0.0)

    def test_partial_match(self):
        text1 = "the quick brown fox jumped over the lazy dog and ran away"
        text2 = "the quick brown fox jumped over the fence"
        result = calculate_similarity(text1, text2)
        self.assertGreater(result['similarity_score'], 0.0)
        self.assertLess(result['similarity_score'], 100.0)

    def test_empty_text1(self):
        result = calculate_similarity("", "some text here to compare against")
        self.assertEqual(result['similarity_score'], 0.0)

    def test_empty_text2(self):
        result = calculate_similarity("some text here to compare against", "")
        self.assertEqual(result['similarity_score'], 0.0)

    def test_single_character_match(self):
        text1 = "a"
        text2 = "a"
        result = calculate_similarity(text1, text2)
        self.assertGreaterEqual(result['similarity_score'], 0.0)

    def test_large_text_performance(self):
        text1 = "the quick brown fox jumped over the lazy dog " * 220
        text2 = "the quick brown fox jumped over the lazy dog " * 220
        result = calculate_similarity(text1, text2)
        self.assertGreaterEqual(result['similarity_score'], 0.0)

if __name__ == '__main__':
    unittest.main()