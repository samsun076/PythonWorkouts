import string
"""Solution to chapter 2, exercise 5, beyond 1: Pig Latin, handle capitalization"""


def pig_latin(word):
    if word[0] in 'aeiouAEIOU':
        output = f'{word}way'
    else:
        output =  f'{word[1:]}{word[0]}ay'

    if word[0] in string.ascii_uppercase:
        output = output.capitalize()
    return output


################################3

print(pig_latin('elephant'))
print(pig_latin('dave'))
print(pig_latin('wim'))
print()
print(pig_latin('Wim'))
print(pig_latin('Elephant'))
print(pig_latin('Dave'))
