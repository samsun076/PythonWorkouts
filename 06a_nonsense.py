"""
Take a text file, creating (and printing) a nonsensical sentence from the nth word on each of the first 10 lines, where n is the line number.
"""

def nonsense(file):
    with open(file) as f:
        for line in f:
            print(line, end='')

nonsense('text_file.txt')
