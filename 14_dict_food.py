"""
create a new constant dict, called MENU, representing the possible items you can order at a restaurant. The keys will be strings, and the val- ues will be prices (i.e., integers). You should then write a function, restaurant, that asks the user to enter an order:
--If the user enters the name of a dish on the menu, the program prints the price and the running total. It then asks the user again for their order.
--If the user enters the name of a dish not on the menu, the program scolds the user (mildly). It then asks the user again for their order.
--If the user enters an empty string, the program stops prompting and prints the total amount.
"""

MENU = {'sandwich': 12,
        'tea': 2,
        'coffee': 3,
        'salad': 10,
        'dessert': 5 
}

def restaurant():
    total = 0
    while True:
        order = input('enter an item you would like to order: ').strip()
        
        # if order is empty(empty string), this will break loop
        if not order:
            break

        if order in MENU:
            price = MENU[order]
            total += price
            print(f'{order} costs {MENU[order]} total is {total}')
        else:
            print(f'We are out of {order},  try again. ')

    print(f'\nyour total: {total}')
            
restaurant()
