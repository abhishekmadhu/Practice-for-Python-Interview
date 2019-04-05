def is_palindrome(word):
    if word.lower()[::-1] == word.lower():
        return True
    else:
        return False


print(is_palindrome('Deleveled'))