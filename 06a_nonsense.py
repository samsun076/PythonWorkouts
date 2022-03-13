"""
Take a text file, creating (and printing) a nonsensical sentence from the nth word on each of the first 10 lines, where n is the line number.
"""

# MY SOLUTION

def nonsense(file):
    sentence = []
    for index, line in enumerate(open(file)):
	    words = line.split()
	    if words and index <= 9:
		    sentence.append(words[index])
    return ' '.join(sentence)



#BOOK SOLUTION
def word_per_line(filename):
    """Given a text file, return a sentence from the nth
word for line n, for each of the first 10 lines.
"""
    output = []

    for n, one_line in enumerate(open(filename)):
        words = one_line.split()

        if not words:
            continue

        if n >= 10:
            break

        if n >= len(words):
            output.append(words[-1])
        else:
            output.append(words[n])

    return ' '.join(output)



print(nonsense('text_file.txt'))
print(nonsense('text_file02.txt'))
print(nonsense('text_file03.txt'))
print()
print(word_per_line('text_file.txt'))
print(word_per_line('text_file02.txt'))
print(word_per_line('text_file03.txt'))
