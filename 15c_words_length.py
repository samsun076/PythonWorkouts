"""
Read through a text file on disk. 
Use a dict to track how many words of each length are in the file—that is, 
how many three-letter words, four-letter words, five-letter words, and so on. Display your results.
"""

from collections import defaultdict
from pprint import pprint

def word_lengths(filename):
    output = defaultdict(int)
    for line in open(filename):
        for word in line.split():
            #number_val = str(len(word)) + '_letter_word'
            output[len(word)] += 1
    return output


pprint(word_lengths('text_file04.txt'))
pprint(word_lengths('text_file.txt'))
