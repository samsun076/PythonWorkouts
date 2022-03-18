#book solution.  Had a hard time solving this

def mysum(*items):
    """
       Sum the passed arguments, which should be of the same type.
       The arguments should handle the + operator.
       If passed no arguments, then return an empty tuple.
    """

    if not items:
        print('no args passed in')
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output


l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

s1 = 'abc'
s2 = 'sfg'
s3 = 'ppv'

print(mysum(l1,l2,l3))
print(mysum(s1,s2,s3))
print(mysum(['a',1],['b'],['bb']))
print(mysum())
