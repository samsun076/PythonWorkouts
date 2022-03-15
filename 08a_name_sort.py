"""
Given the string “Tom Dick Harry,” break it into individual words, and then sort those words alphabetically. Once they’re sorted, print them with commas (,) between the names.
"""

# My Solution
def sorted_n(name):
    return ', '.join(sorted(str.split(name)))

# Book Solution
def sorted_words(s):
 return ', '.join(one_word for one_word in sorted(s.split()))

names = ["Tom Dick Harry", "Dave Marcinowski", "John Jingle Heimer Schidmt", "Larry Johnson", "Maddison Kelly Anne"]

for x in names:
    print(sorted_n(x))
    print(sorted_words(x))
    print()
