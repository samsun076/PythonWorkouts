import string
"""Solution to chapter 2, exercise 5, beyond 1: Pig Latin, handle capitalization"""


def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'

print(pig_latin('elephant'))
print(pig_latin('dave'))
