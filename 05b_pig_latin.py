import string
"""
Solution to chapter 2, exercise 5, beyond 1: Pig Latin, handle capitalization
adding logic to handle punction to be moved to end of word!"

"""


def pig_latin(word):
    punct = ''
    if word[-1] in string.punctuation:
        punct=word[-1]
        output = word[:-1]
    else:
        output = word

    if output[0].lower() in 'aeiou':
        output = f'{output}way{punct}'
    else:
        output =  f'{output[1:]}{output[0]}ay{punct}'
    
    # need to check original word against uppercase.  This is pre transformation.
    if word[0] in string.ascii_uppercase:
        output = output.lower().capitalize()
    return word,output


################################

print(pig_latin('elephant'))
print(pig_latin('dave'))
print(pig_latin('wim'))
print()
print(pig_latin('Wim'))
print(pig_latin('Elephant'))
print(pig_latin('Dave'))
print()

print(pig_latin('Dave!'))
print(pig_latin('dave!'))
print(pig_latin('elephant!'))
print(pig_latin('Elephant!'))
