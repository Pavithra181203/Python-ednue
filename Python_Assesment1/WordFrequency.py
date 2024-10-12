import string
def word_frequency(sentence):
    normalize_sentence = sentence.lower().translate(str.maketrans('', '', string.punctuation))
    words = normalize_sentence.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency
sentence = "Hello world @ Hello"
result = word_frequency(sentence)
print(result)
