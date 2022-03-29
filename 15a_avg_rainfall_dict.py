"""
Instead of printing just the total rainfall for each city, print the total rainfall and the average rainfall for reported days. Thus, if you were to enter 30, 20, and 40 for Boston, you would see that the total was 90 and the average was 30.

"""

# MY SOLUTION
def get_rainfall():
    city_rainfall = {}
    while True:
        city = input('Enter a city name: ').strip()
    
        if not city:
            break

        amount = int(input('enter the amount of rainfall in mm: ').strip())
        
        city_rainfall.setdefault(city, []).append(amount)
        sum_rain = sum(city_rainfall[city]) 
        avg_rain = sum_rain / len(city_rainfall[city])
    for city in city_rainfall:
        print(f'{city}: SUM: {sum_rain} AVG: {avg_rain}')
get_rainfall()

# BOOK SOLUTION
def get_rainfall():
    rainfall = {}
    
    while True:
        city_name = input('Enter a City name: ')
    
        if not city_name:
            break

        mm_rain = input('Enter mm rain: ')

        if city_name not in rainfall:
            rainfall[city_name] = []
    
        rainfall[city_name].append(int(mm_rain))

    for city, rain in rainfall.items():
        print(f'{city}: Total {sum(rain)}, Average {sum(rain)/len(rain)}')


get_rainfall()    
