"""
Write a function, dictdiff, that takes two dicts as arguments. 
The function returns a new dict that expresses the difference between the two dicts.

If there are no differences between the dicts, dictdiff returns an empty dict.

or each key-value pair that differs, the return value of dictdiff will have a key-value pair in which the value is a list containing the values from the two different dicts.

f one of the dicts doesn’t contain that key, it should contain None. 
"""

d1 = {"a":1, "b":2, "c":3}
d2 = {"a":1, "b":2, "c":3}
d3 = {"a":1, "b":2, "c":4}
d4 = {"a":1, "b":2, "d":4}

def dictdiff(dict1, dict2):
    output = {}
    all_keys = dict1.keys() | dict2.keys()

    for key in all_keys:
        if dict1.get(key) != dict2.get(key):
            output[key] = [dict1.get(key), dict2.get(key)]
    return output
print(dictdiff(d1, d2))
print(dictdiff(d1, d3))
print(dictdiff(d3, d4))

