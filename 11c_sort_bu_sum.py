
"""Given a list of lists, in which the inner lists contain
numbers, return the outer list sorted by each inner list's sum.
"""

def sort_by_sum(list_of_lists):
    return sorted(list_of_lists, key=sum)

print([10,20,40,50],[10],[-10,-10],[100,-1000])
