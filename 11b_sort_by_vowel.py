"""
Given a list of strings, sort them according to how many vowels they contain.
"""

#book solution

def word_vowel_count(word):
    total = 0
    for letter in word:
        if letter in 'aeiou':
            total += 1
    return total

def sort_words_by_vowel(words):
    return sorted(words, key=word_vowel_count)

my_words = ["pickles", "wookie", "sunny", "dave", "supercalafragile","leslie", "parker"]
print(sort_words_by_vowel(my_words))
