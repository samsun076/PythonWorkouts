"""
you’ll write a function (called ubbi_dubbi) that takes a single word (string) as an argument. It returns a string, the word’s translation into Ubbi Dubbi. So if the function is called with octopus, the function will return the string uboctubopubus. And if the user passes the argument elephant, you’ll output ubelubephubant.
"""


def ubbi(word):
	ubbi =[]
	for letter in word:
		if letter in 'aeiou':
			ubbi.append(f'ub{letter}')
		else:
			ubbi.append(letter)
	return ''.join(ubbi)


print(ubbi('octopus'))
print(ubbi('elephant'))
print()
print(ubbi('octopus') == 'uboctubopubus')
print(ubbi('elephant') == 'ubelubephubant')
