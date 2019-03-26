# A function to test
def get_full_name(first, last, middle=''):
	"""Return a full name."""
	if middle:
		name = f'{first} {middle} {last}'
	else:
		name = f'{first} {last}'
	return name


# Using the function
paavan = get_full_name('Paavan', 'R',  'Gopala')
print(paavan)

manju = get_full_name('Manjula', 'A', 'Subramanyam')
print(manju)
