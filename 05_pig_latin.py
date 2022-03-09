"""
Write a function called pig_latin that takes a string as input ( assumed to be english)
The function will return the translation of the string in pig latin

assum no capital letters or punctuation.

If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the word. So “air” becomes “airway” and “eat” becomes “eatway.”

If the word begins with any other letter, then we take the first letter, put it on the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay” and “computer” becomes “omputercay.”
"""
# Here I did not follow the requirments and added the functionality of a string which turns out is 
# exercise6.
# MY SOLUTION

def pig_latin():
    my_string = input("Enter a sting to convert into Pig Latin: ")
    vowels = 'aeiou'
    pig_string = ''
    for word in my_string.split():
        if word[0] in vowels:
            pig_string += word + 'ay '
        else:
            pig_string += word[1:] + word[0] + 'ay '
    return pig_string


# BOOK SOLUTION
def pig_latin2(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

print(pig_latin())
print()
print(pig_latin2("Another"))
print(pig_latin2("David"))
