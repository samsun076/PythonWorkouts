"""
write a function that takes a float and 2 integers (before and after)
the function should return a float consisting of before digits before the decimal
and after digits after.
1234.5678, 2, 3 should return 34.567
"""

def before_after_dot(f, before, after):
    s = str(f)
    i = s.index('.')
    #print(i-before, i+after+1)
    return s[i-before:i+after+1] #per the example in the comments, this will evaluate to s[3:5]

print(before_after_dot(1234.5678,2,3))
print(before_after_dot(27.345734534,1,4))
