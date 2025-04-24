def is_palindrome(text: str) -> bool:
    return text == text[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False