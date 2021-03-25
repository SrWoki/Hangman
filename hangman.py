from words import words
import random

print("Welcome to the hangman game in Python")

def get_valid_word(words):
    word = random.choice(words)

    # Choose a good word
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

hidden_word = set()
hidden_word.add('-')
for letter in get_valid_word(words):
    print('-')
print(set(get_valid_word(words)))