"""
Which is the last word, alphabetically, in a text file?
"""

def last_word_alphabetically(file):
    
    """
    Given the name of a text file,
    return the word that comes last (alphabetically)
    in that file.
    """
    output = ""
    for one_line in open(file):
        for one_word in one_line.split():
            if not one_word.isalpha():
                continue
            if one_word > output:
                output = one_word
    return output

print(last_word_alphabetically('text_file04.txt'))
print(last_word_alphabetically('text_file.txt'))
