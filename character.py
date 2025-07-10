def is_palindrome(s):
    s_clean = ''.join(c.lower() for c in s if c.isalnum())
    return s_clean == s_clean[::-1]
