'''
Define a dict whose keys are dates (represented by strings) from the most recent week - YYYY-MM-DD format
and whose values are temperatures. 
Ask the user to enter a date, and display the temperature on that date, as well as the previous and subsequent dates, if available.
'''
from datetime import datetime, timedelta
TEMPS= {'2022-03-01': 44,
         '2022-03-02': 33,
         '2022-03-03': 65,
         '2022-03-04': 55,
         '2022-03-05': 54,
         '2022-03-06': 53,
         '2022-03-07': 37,
}


def get_temp():
    while True:
        user_date = input("Enter a date in YYYY-MM-DD format: ").strip() 

        if not user_date:
            print("ABORTING")
            break
        if len(user_date) != 10:
            print("format incorrect, try again: ")
            continue

        if user_date.count('-') != 2:
            print("Please use the correct delimter: ")
            continue

        if user_date not in TEMPS:
            print(f'{user_date} is invalid, try a different one: ')
            continue

        try:
            date = datetime.fromisoformat(user_date).date()
        except ValueError as e:
            print("Not a valid date string, try again: ")
            continue
        previous_day = str(date + timedelta(1))
        next_day = str(date - timedelta(1))
     
        print(f'\nprevious date: {previous_day} -- TEMP: {TEMPS.get(previous_day, "no date entry exists")}')
        print(f'reqested date: {date} -- TEMP: {TEMPS[str(date)]}')
        print(f'next date: {next_day} -- TEMP: {TEMPS.get(next_day, "No date entry exists")}\n')

get_temp()

