import operator
"""
write a function, alphabetize_names, that assumes the existence of a PEOPLE constant defined as shown in the code. The function should return the list of dicts, but sorted by last name and then by first name.
"""

PEOPLE = [{'first':'Reuven', 'last':'Lerner',
    'email':'reuven@lerner.co.il'},
 {'first':'Joseph', 'last':'Biden',
'email':'president@whitehouse.gov'},
 {'first':'David', 'last':'Marcinowski',
    'email':'davemarcinowski@gmail.com'},
 {'first':'Leslie', 'last':'Bebb',
'email':'LeslieBebb@gmail.com'}
 ]

def alphabetize(contacts):
    return sorted(contacts, key=operator.itemgetter('last', 'first'))

for person in alphabetize(PEOPLE):
    print(f'{person["last"]},  {person["first"]} :: { person["email"]}')
