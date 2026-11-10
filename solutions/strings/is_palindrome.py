"""Palindrome check after normalizing to lowercase letters and digits.

A palindrome is a word, phrase, or sequence that reads the same forward
and backward. Examples: "madam", "level", and "racecar". The phrase
"A man, a plan, a canal: Panama" is also a palindrome once spaces,
punctuation, and letter casing are ignored.

This module provides :func:`is_palindrome`, which applies that same
normalization rule before comparing the string with its reverse.
"""


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forward and backward.

    The check has two steps:

    1. **Normalize** the input by keeping only alphanumeric characters
       and converting them to lowercase. This is why uppercase letters
       do not matter: ``"Madam"`` and ``"madam"`` are treated the same.
       Spaces, punctuation, and symbols are dropped, so
       ``"A man, a plan, a canal: Panama"`` becomes
       ``"amanaplanacanalpanama"``.
    2. **Compare** the normalized string with its reverse. If they are
       equal, the original text is a palindrome.

    Examples
    --------
    >>> is_palindrome("madam")
    True
    >>> is_palindrome("level")
    True
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True

    Parameters
    ----------
    text:
        The string to check. It may contain any characters.

    Returns
    -------
    bool
        ``True`` if ``text`` is a palindrome under the normalization
        rule described above, ``False`` otherwise.

    Complexity
    ----------
    - **Time:** O(n), where *n* is the length of ``text``. Each
      character is visited a constant number of times.
    - **Space:** O(n), because the normalized string is built in
      memory before the reversed comparison.
    """
    normalized = "".join(char.lower() for char in text if char.isalnum())
    return normalized == normalized[::-1]
