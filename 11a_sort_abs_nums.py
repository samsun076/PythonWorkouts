"""
Given a sequence of positive and negative numbers, sort them by absolute value.
"""


def sort_abs(my_list):
    return sorted(my_list, key=abs)


nums = [-16, 88, 100, -100, 1,2,-3,-4,-5,]
print(sort_abs(nums))
