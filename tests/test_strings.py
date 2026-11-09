from solutions.strings.is_palindrome import is_palindrome

def test_palindrome_simple():
    assert is_palindrome("level") is True

def test_palindrome_ignores_case_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_non_palindrome():
    assert is_palindrome("python") is False

def test_empty_normalized_string():
    assert is_palindrome("...") is True
