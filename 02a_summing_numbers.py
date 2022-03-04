
def mysum(num_list, start=0):
    """
    adds optional second argument, used as starting point for summing.
 
    """
    total = start
    print()
    print('starting at: ', total)
    for x in num_list:
        total += x
    return total

print(mysum([1,2,3,4,5,6,7,8,9]))
print(mysum([1,2,3,4,5,6,7,8,9], 5))
