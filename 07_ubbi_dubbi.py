"""
you’ll write a function (called ubbi_dubbi) that takes a single word (string) as an argument. It returns a string, the word’s translation into Ubbi Dubbi. So if the function is called with octopus, the function will return the string uboctubopubus. And if the user passes the argument elephant, you’ll output ubelubephubant.
"""

#My solution
def ubbi(word):
    ubbi =[]
    for letter in word:
        if letter in 'aeiou':
            ubbi.append(f'ub{letter}')
        else:
            ubbi.append(letter)
    return ''.join(ubbi)


# Book Solution

def ubbi2(word):
	output = ''
	for letter in word:
		if letter in 'aeiou':
			output += f'ub{letter}'
		else:
			output += letter
	return output


print("My Solution")
print(ubbi('octopus'))
print(ubbi('elephant'))
print()
print(ubbi('octopus') == 'uboctubopubus')
print(ubbi('elephant') == 'ubelubephubant')
print("Book Solutuion")
print()
print(ubbi2('octopus'))
print(ubbi2('elephant'))
print()
print(ubbi2('octopus') == 'uboctubopubus')
print(ubbi2('elephant') == 'ubelubephubant')
