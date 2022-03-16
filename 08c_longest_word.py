"""
Which is the longest word in a text file?
"""
def longest_word(file):
    word_length = 0
    for line in open(file):
        for word in line.split():
            if len(word) > word_length:
                word_length = len(word)
    return word_length, word
   
print(longest_word("text_file.txt"))
