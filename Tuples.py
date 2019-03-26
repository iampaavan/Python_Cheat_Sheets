dimensions = (800, 600, 300, 400, 500, 400)
print('List of Tuples: ', dimensions)

for dimension in dimensions:
	print('List of Tuple one by one: ', dimension)

print('List the first element of the Tuple: ', dimensions[0])
print()
print('Get the last element of the tuple: ', dimensions[-1])

print('Count how many times 400 is present in the tuple: ', dimensions.count(400))
print()

print('Get the index value of 400: ', dimensions.index(400))
