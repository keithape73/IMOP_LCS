import unittest
from imop_lcs import imop_lcs

class TestIMOPLCS(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(imop_lcs("abcde", "ace"), 3)
        self.assertEqual(imop_lcs("abcabcabc", "abcabc"), 6)
        self.assertEqual(imop_lcs("aaaaa", "aaa"), 3)
        self.assertEqual(imop_lcs("xyz", "xyz"), 3)
        self.assertEqual(imop_lcs("abc", "def"), 0)
        self.assertEqual(imop_lcs("abacaba", "axbya"), 3)  # "aba"

    def test_repeated_chars(self):
        self.assertEqual(imop_lcs("aabbaacc", "abcabc"), 4)
        self.assertEqual(imop_lcs("aaaa", "aa"), 2)

    def test_edge_cases(self):
        self.assertEqual(imop_lcs("", ""), 0)
        self.assertEqual(imop_lcs("a", ""), 0)
        self.assertEqual(imop_lcs("", "b"), 0)
        self.assertEqual(imop_lcs("a", "a"), 1)
        self.assertEqual(imop_lcs("a" * 1000, "a" * 500), 500)

if __name__ == "__main__":
    unittest.main()
