"""
Define a list of tuples, in which each tuple contains the name, length (in min- utes), and director of the movies nominated for best picture Oscar awards last year. Ask the user whether they want to sort the list by title, length, or director’s name, and then present the list sorted by the user’s choice of axis.
"""

from operator import itemgetter

MOVIES = [('Parasite', 132, 'Bong Joon-ho'),
          ('Ford v Ferrari', 152, 'James Mangold'),
          ('The Irishman', 209, 'Martin Scorsese'),
          ('Jojo Rabbit', 108, 'Taika Waititi'),
          ('Joker', 122, 'Todd Phillips'),
          ('Little Women', 135, 'Greta Gerwig'),
          ('Marriage Story', 137, 'Noah Baumbach'),
          ('1917', 119, 'Sam Mendes'),
          ('Once Upon a Time in Hollywood', 161, 'Quentin Tarantino')
          ]

FIELDS = {
    'name': 0,
    'length': 1,
     'director': 2}

def sort_movies():
    sort_by = input("Enter a sort field - name/length/director - ").strip()

    if sort_by in FIELDS:
        output = []
        template = "{0:30} {1:3} {2:20}"
        for one_movie in sorted(MOVIES, key=itemgetter(FIELDS[sort_by])):
            output.append(template.format(*one_movie))
        return output

print('\n'.join(sort_movies()))
    
