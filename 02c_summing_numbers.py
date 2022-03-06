
#solution01 - me
def word_math(word_list):
    """
    take a list of words, return a tuple containing three integers, 
    length of shortest word, longest, and average length

    """
    word_list2 = []
    word_length= []
    for word in word_list:
        word_list2.append((len(word), word))
        word_length.append(len(word))
    word_list2.sort()
    
    longest = word_list2[-1][1]
    shortest = word_list2[0][1]
    average = sum(word_length)/len(word_length)

    
    return longest, shortest, average

print(word_math(['dave', 'leslieBebb', 'parkerM', 'wookT', 'yinzer', 'slicker', 'sunsunMgunn', 'pix']))


#solution02 - book
def summerize(words):
    """
    """
    word_lengths = [len(word) for word in words]

    return max(word_lengths), min(word_lengths), sum(word_lengths)/len(word_lengths)

print(summerize(['dave', 'leslieBebb', 'parkerM', 'wookT', 'yinzer', 'slicker', 'sunsunMgunn', 'pix']))
