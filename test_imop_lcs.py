# test_imop_lcs.py

from imop_lcs import imop_lcs

def test_basic():
    assert imop_lcs("abcde", "ace") == 3
    assert imop_lcs("abcabcabc", "abcabc") == 6
    assert imop_lcs("aaaaa", "aaa") == 3
    assert imop_lcs("xyz", "xyz") == 3
    assert imop_lcs("abc", "def") == 0
    assert imop_lcs("abacaba","axbya") == 3 #("aba")

def test_edge_cases():
    assert imop_lcs("", "") == 0
    assert imop_lcs("a", "") == 0
    assert imop_lcs("", "b") == 0
    assert imop_lcs("a", "a") == 1
    assert imop_lcs("a"*1000, "a"*500) == 500

if __name__ == "__main__":
    test_basic()
    test_edge_cases()
    print("✅ All tests passed!")
