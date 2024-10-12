def is_palindrome(word: str):
    word=input("Enter a word: ")
    normalized_word = word.replace(" "," ").lower()
    return normalized_word == normalized_word[::-1]
