
"""
Solution to chapter 1, exercise 4, beyond 2: name_triangle
write a function that creates a name triangle
"""


# MY SOLUTION
def name_tri1():
    total = ''
    name = input('Enter a name: ')
    for char in name:
        total += char
        print(total)

name_tri1()



# BOOK SOLUTION
def name_tri2():
    name = input("enter a name: ")
    for char in range(len(name)):
        print(name[:char+1])

name_tri2()
