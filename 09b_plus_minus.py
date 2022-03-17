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
