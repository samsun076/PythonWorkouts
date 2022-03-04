
def word_math(word_list):
    """
    take a list of words, return a tuple containing three integers, 
    length of shortest word, longest, and average length

    """
    total = 0
    
    print()
    for word in word_list:
        print(word, " - characters -", len(word))
        for char in word:
            print(char)
    print(len(word_list))

print(word_math(['dave', 'leslie', 'parker', 'wookie', 'yinzer', 'slick', 'sunny', 'pickles']))
