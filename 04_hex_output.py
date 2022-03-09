"""
wirte a function called (hex_output) that takes a hex number and returns the decimal equivalent
if a user enters 50, youll assum its a hex equal to 0x50 and will return a value of 80

"""
def hex_output(hexnum):
    total = 0
    for index, num in enumerate(reversed(hexnum)):
        total += int(num, 16) * 16 ** index  #enter second option argument in int function
        print(f'{num} * 16 ** {index}: {total}')
    print()



hex_output('1357')
hex_output('ff')
hex_output('3eafd')


#https://www.askpython.com/python/built-in-methods/python-chr-and-ord-methods
