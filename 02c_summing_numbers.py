"""
write a function that takes a list of python objects.
sum the objects that either are integers, or can be turned into integers
ignoring the others
"""
#My solution
def sum_of_int(numbers):
    int_list = []
    
    for item in numbers:
        try:
            an_integer = isinstance(item, int)
            
            #if not an an integer but a str, such as "6", convert to INT and add to list
            #else it should be an integer, so add to list
            #throw an Exception if number is a non convertable string such as "seven"
            if not an_integer:
                int_list.append(int(item))
            else:
                int_list.append(item)
        except Exception as err:
            err
            #print("Can not convert to INT. ", str(err))
    return sum(int_list)




print(sum_of_int([1,2,3,4,5,"6", "seven"]))
print(sum_of_int([1.2,2.0,3.0,]))
print(sum_of_int([1,2,3,4,5,6,7,8,9]))
print(sum_of_int(["1","2","3","4","5","6","7","8","9"]))
print(sum_of_int(["1","2","3","4","5","6","7","8","9.0"]))


#BOOK Solution - NOT Working
def is_integer(one_item):
    """
    function that takes an item and converts it to an integer
    if it can not be converted it throws a Value error and returns false
    string of "7" will be converted to 7 and return True
    string of "seven" will not be converted and throw the Value error
    """
    try:
        int(one_item)
        return True
    except ValueError:
        return False

def sum_of_int2(items):
    return sum(int(one_item) for one_item in items if is_integer(one_item))


print()

print(sum_of_int2(["1",2,3,4,5,6,7,8,9]))
print(sum_of_int2([1,2,3,4,5,"6", "seven"]))
