"""
Instead of finding the word with the greatest number of repeated letters, find the word with the greatest number of repeated vowels.

Write a function, most_repeating_word, that takes a sequence of strings as input. The function should return the string that contains the greatest number of repeated letters."""


from collections import Counter

def most_repeating_vowel(word):
    total = 0
    for letter in word:
        if letter in 'aeiou':
            total += 1
    return total

def word_with_most_vowels(list_of_words):
    return max(list_of_words, key=most_repeating_vowel) 
print(most_repeating_vowel('asscrack'))

my_list = ['mississippi','tweak','twerk','my','weed','testing']
print(word_with_most_vowels(my_list))

