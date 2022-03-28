"""
Define a dict whose keys are names of people in your family, 
and whose values are their birth dates, as represented by Python date objects (http://mng.bz/ jggr). 
Ask the user to enter the name of someone in your family, 
and have the program calculate how many days old that person is.
"""
from datetime import datetime

FAMILY = {'Leslie Bebb': '1979-09-02',
          'Parker Marcinowski': '2012-04-08',
          'Dave Marcinowski': '1980-04-03',
          'Pickles': '2021-02-15',
          'Sunny': '2019-06-06',
        }

def days_old():
    while True:
        person = input("Please enter a name: ").strip()
    
        if not person:
            break

        if person not in FAMILY:
            print(f'{person} is not a valid name, try again: ')
        birthday = datetime.fromisoformat(FAMILY[person])
        today = datetime.now()
        days_old = today.date() - birthday.date()
        print(f"{person} was born on {FAMILY[person]} and is {days_old.days} days old")
        break
days_old()
