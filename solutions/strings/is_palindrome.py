"""Palindrome check after normalizing to lowercase letters and digits."""

def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forward and backward.

    Non-alphanumeric characters are ignored.
    Time: O(n); Space: O(n) for the normalized string.
    """
    normalized = "".join(char.lower() for char in text if char.isalnum())
    return normalized == normalized[::-1]
