
vowels = ['a', 'o', 'u', 'i', 'y', 'e']


def remove_vowels(word):
    new_word = ''
    for letter in word:
        if letter.lower() not in vowels:
            new_word += letter
    return new_word.capitalize()

print(remove_vowels('AAAAAAAAAAAAggggg'))