<<<<<<< HEAD
"""Solution to chapter 3, exercise 9, beyond 5: plus_minus"""
#Book Solution
# Having a hard time following the logic when adding print statements to look through 
# the loop sequene.
# TODO - Further look into while loops 

def plus_minus(numbers):
    """Takes a list of numbers, and returns the result
of alternately adding and subtracting them.
"""
    if not numbers:
        return 0

    total = numbers.pop(0)
    while numbers:
        total += numbers.pop(0)
        
        if numbers:
            total -= numbers.pop(0)
    return total


num = [10,20,30,40,50,60]
num2 = [10,20,30,40,50,60,70,80,90,100,110]

print(plus_minus(num))
print(plus_minus(num2))

#
=======
"""
Write a function that takes a list or tuple of numbers. Return the result of alternately adding and subtracting numbers from each other. So calling the function as plus_minus([10,20,30,40,50,60]), you’ll get back the result of 10+20-30+40-50+60, or 50.

"""

def plus_minus(numbers):
    for x in numbers:
        if x

num = [10,20,30,40,50,60]
print(plus_minus(num))
>>>>>>> 64455be703ca29c35571b07131898deb81ea63ba
