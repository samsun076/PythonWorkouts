"""
Take a text file, creating (and printing) a nonsensical sentence from the nth word on each of the first 10 lines, where n is the line number.
"""

def nonsense(file):
    for index, line in enumerate(open(file)):
        words = line.split()
        if words:
            print(index, words[0])

nonsense('text_file.txt')
