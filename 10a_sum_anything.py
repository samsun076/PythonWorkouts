"""
Write a function, mysum_bigger_than, that works the same as mysum, except that it takes a first argument that precedes *args. That argument indicates the threshold for including an argument in the sum. Thus, calling mysum_bigger _than(10, 5, 20, 30, 6) would return 50—because 5 and 6 aren’t greater than 10. This function should similarly work with any type and assumes that all of the arguments are of the same type. Note that > and < work on many different types in Python, not just on numbers; with strings, lists, and tuples, it refers to their sort order.
"""

def mysum_bigger_than(num, *args):
    print(f'your num: {num} and ARGS: {args}')



mysum_bigger_than(60, [50,60,70,80,90,100])

