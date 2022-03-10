"""
translate a series of words into pig latin. 
do not have to account for punctuation or capitals

'this is a test translation'
would be
histay isway away estay ranslationtay

"""

#MY SOLUTION
def pl_sentence():
    sentence = input("Enter a sentenct to convert: ")
    vowels = 'aeiou'
    new_phrase = []
    for word in sentence.split():
        if word[0] in vowels:
            new_phrase.append(word + 'way')
        else:
            new_phrase.append(word[1:] + word[0] + 'ay')
    return ' '.join(new_phrase)
            
# BOOK SOLUTION
# SAME CONCEPT EXCEPT BOOK USED F STRINGS INSTEAD OF PRINT
def pl_sentence2(sentence):
    """
       Get a sentence from the user, containing
       lowercase, unpuncutated words. Return the
       sentence, translated into Pig Latin.
    """
    output = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
    return " ".join(output)


print(pl_sentence())
print(pl_sentence2('this is a test translation'))
