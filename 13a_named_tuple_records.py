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

def sorted_named_tuple(list_of_tuples):
    output = []
    template = '{last:15} {first:10} {distance:5.2f}'
    for person in sorted(list_of_tuples, key=attrgetter('last', 'first')):
        output.append(template.format(**(person._asdict())))
        #output.append(person._asdict())
    return output

print('\n'.join(sorted_named_tuple(PEOPLE)))
