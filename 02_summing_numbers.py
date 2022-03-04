
def mysum(*args):
    """
    function that does same thing as BIF sum.  
    accepts any number of numeric arguments and returns sum of those numbers
    if invoked without any arguments, will return 0
    """
    total = 0
    print()
    print('starting at: ', total)
    for x in args:
        total += x
    return total

print(mysum(10,20,30))
print(mysum(10,10))
print(mysum(*[1,2,3,4,5,6,7,8,9]))
