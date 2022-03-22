"""
Write a program to read /etc/passwd on a Unix computer. The first field contains the username, and the final field contains the user’s shell, the command inter- preter. Display the shells in decreasing order of popularity, such that the most pop- ular shell is shown first, the second most popular shell second, and so forth.
"""
from collections import Counter
from operator import itemgetter


# figured out counter logic and list comp on my own.
# needed help with the sorted piect

# Logic - list comp creates a list called shell
# for loop iterate through each line within file
# if line does not contatin '#'
# return the last item within the index from the list created by the split method delimited by ':'

def find_shell_count(filename):
    shells = Counter([line.split(':')[-1].strip() 
                              for line in open(filename) 
                              if '#' not in line])
    return sorted(shells, key=itemgetter(1), reverse=True)


# BOOK SOLUTION - slightly different.  
# Usese setcomp instead of listcomp. 
# logic dealing with '#' is slightly different.

def shells_by_popularity(filename):
    shells = Counter(one_line.split(':')[-1].strip() 
                     for one_line in open(filename) 
                     if not one_line.startswith(('#','\n')))
    return sorted(shells.items(), key=itemgetter(1), reverse=True)

print(find_shell_count('/etc/passwd'))
print(shells_by_popularity('/etc/passwd'))



