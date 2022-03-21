"""
Write a function that takes a list of dicts and returns a single dict that combines all the keys and valuess.  If a key appers in more than one argument, the value should be a listing containing all the values from the arguments.
"""

#book solution
#need to work through some of the dict logic

def combine_dicts(*args):
    output = {}
    for x in args:
        for key, value in x.items():
            if key in output:
                try:
                    output[key].append(value)
                except AttributeError:
                    output[key] = [output[key], value]
            else:
                output[key] = value
        print()
    return output

print(combine_dicts({'apples': 20, 'oranges': 10}, {'dogs': 1, 'crows': 3, 'turkeys': 9}))
print('*' * 60)
print(combine_dicts({'dogs': 3, 'apples': 20, 'oranges': 10}, {'dogs': 1, 'crows': 3, 'turkeys': 9}))

