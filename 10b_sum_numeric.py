"""
Write a function, sum_numeric, that takes any number of arguments. If the argument is or can be turned into an integer, then it should be added to the total. Arguments that can’t be handled as integers should be ignored. The result is the sum of the numbers. Thus, sum_numeric(10, 20, 'a', '30', 'bcd') would return 60. Notice that even if the string 30 is an element in the list, it’s converted into an integer and added to the total.
"""

def sum_numeric(*items):
    total = 0
    for item in items:
        try:
            total += int(item)
            print('adding', item)
        except ValueError:
            pass
    return total



print(sum_numeric(10,20,'30','Aabc'))
print(sum_numeric(10,'-20','30','Aabc'))
