def count_vowels_consonants(word: str) :
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0

    for char in word:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return {'vowels': vowel_count, 'consonants': consonant_count}

# Example usage
result = count_vowels_consonants("Hello World")
print(result)
