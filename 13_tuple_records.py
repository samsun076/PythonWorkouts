"""This function expects to get a list
of tuples, each representing a person.
Each tuple contains three elements -- first
name, last name, and distance to travel.
(The first two are strings, and the third is
a float.)  We return a list of strings,
sorted by last name and then first name.
"""

from operator import itemgetter

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(list_of_tuples):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(list_of_tuples, key=itemgetter(1,0)):
        output.append(template.format(*person))
    return output


print('\n'.join(format_sort_records(PEOPLE)))
