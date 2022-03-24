"""This function expects to get a list
of tuples, each representing a person.
Each tuple contains three elements -- first
name, last name, and distance to travel.
(The first two are strings, and the third is
a float.)  We return a list of strings,
sorted by last name and then first name.
"""


from operator import attrgetter
from collections import namedtuple

Person = namedtuple('Person',['first','last','distance'])

PEOPLE = [Person('Rich','Marcinowski',77.7986),
          Person('Dave','Marcinowski',98.9986),
          Person('Leslie', 'Bebb', 44.221), 
          Person('Parker', 'Marcinowski', 11.2234), 
          Person('Todd','Bebb',66.33253), 
          Person('Arnold', 'Palmer', 77.03902), 
          Person('Phil','Marcinowski',77.4322), 
          Person('Alicia','Marcinowski',99.3342)]


def sort_named_tuple(list_of_tuples):
    output = []
    template = '{last:10} {first:10} {distance:5.2f}'
    for person in sorted(list_of_tuples, key=attrgetter('last', 'first')):
        output.append(template.format(*(person._asdict())))
    return output

print(sort_named_tuple(PEOPLE))
