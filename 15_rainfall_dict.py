"""
write a function, get_rainfall, that tracks rainfall in a number of cities.

Users of your program will enter the name of a city;

If the city name is blank, then the function prints a report (which I’ll describe) before exiting.

If the city name isn’t blank, then the program should also ask the user how much rain has fallen in that city (typically measured in millimeters).

After the user enters the quantity of rain, the program again asks them for a city name, rainfall amount, nd so on—until the user presses Enter instead of typing the name of a city.

When the user enters a blank city name, the program exits—but first, it reports how much total rainfall there was in each city. Thus, if I enter
Boston
5

New York
7

Boston
5

[Enter; blank line]

the program should output:
Boston: 10
New York: 7


"""

# MY SOLUTION
def get_rainfall():
    city_rainfall = {}
    while True:
        city = input('Enter a city name: ').strip()
    
        if not city:
            break

        amount = input('enter the amount of rainfall in mm: ').strip()
        
        # setdefault used in my solution
        city_rainfall.setdefault(city, 0)
        city_rainfall[city] += int(amount)
    
        # Book solution
        # alternatively the dict.get method can be used with two arguments
        # city_rainfall[city] = city_rainfall.get(city, 0) + int(amount)

        # defaultdict from collections can be imported and used as well.
    for k, v in city_rainfall.items():
        print(f'{k}: {v}')
get_rainfall()
