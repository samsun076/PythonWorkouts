"""
Write a function, most_repeating_word, that takes a sequence of strings as input. The function should return the string that contains the greatest number of repeated letters.
"""

from collections import Counter

# Create function to get the most common occurance of a letter in a provided word
def common_letter_count(word):
    return Counter(word).most_common(1)[0][1]


# function that ouputs the word with the most occurances of a letter
# can be done with the sorted function as well and using -1 of the index to call the last item.
# key is used to call the common_letter_count function as the parameter to sort by.
  
def most_repeating_word(words):
    #return sorted(word, key=common_letter_count)[-1]
    return max(words, key=common_letter_count)

print(common_letter_count('whoops'))
words = ['faantaasticaal', 'a', 'aa', 'dave', 'wookie', 'zzzz']
print(most_repeating_word(words))

