"""
Write a function that takes a list or tuple of numbers. Return a two-element list, containing (respectively) the sum of the even-indexed numbers and the sum of the odd-indexed numbers. So calling the function as even_odd_sums([10, 20, 30,40,50,60]), you’ll get back[90,120].
"""

#my solution

def sum_odds_evens(my_list):
    return [sum(t[0::2]), sum(t[1::2])]

#issues with using and reproducing the book solution. 03/16/22.
def sum_odds_evens1(numbers):
    evens = []
    odds = []

    for one_number in numbers:
        if one_number % 2:
            odds.append(one_number)
        else:
            evens.append(one_number)
    return [sum(odds), sum(evens)]

t = [10,20,30,40,50,60]
print(sum_odds_evens(t))
print(sum_odds_evens1(t))
            
