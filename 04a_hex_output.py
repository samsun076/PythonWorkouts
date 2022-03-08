"""
wirte a function called (hex_output) that takes a hex number and returns the decimal equivalent
if a user enters 50, youll assum its a hex equal to 0x50 and will return a value of 80

addition of user unput
"""

def hex_output():
    hex_response = input("Enter a HEX number to be converted to Decimal: ")
    total = 0
    for power, number in enumerate(reversed(hex_response)):
        total += int(number, 16) * 16 ** power
        print(f'{number} * 16 ** {power}: {total}')


hex_output()
