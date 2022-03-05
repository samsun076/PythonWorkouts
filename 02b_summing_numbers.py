# taking the sum and average of the list of numbers

def mysum(num_list, start=0):
    """
    adds optional second argument, used as starting point for summing.
    added giving the average of the list 

    """
    total = start
    
    print()
    print('starting at: ', total)
    for x in num_list:
        total += x
    average = total/len(num_list)
    print("sum:", total, "\taverage:", average)

print(mysum([1,2,3,4,5,6,7,8,9]))
print(mysum([1,2,3,4,5,6,7,8,9], 5))
