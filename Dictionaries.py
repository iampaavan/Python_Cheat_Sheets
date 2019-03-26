# A simple dictionary
alien = {'color': 'green', 'points': 5}

# Accessing a value
# print('The alien\'s color is ' + alien['color'] + '.')
# print('The alien\'s color is {}.'.format(alien['color']))
print(f"The alien\'s color is {alien['color']}.")

# Adding a key-value pair
alien['x_position'] = 0
print(alien)

# Looping through all key-value pair's
fav_numbers = {'Eric': 17, 'Ever': 4}
for name, number in fav_numbers.items():
	print(name + ' loves ' + str(number))

print()

# Looping through all keys
for name in fav_numbers.keys():
	print(name + ' loves a number ')

print()

# Looping through all values
for number in fav_numbers.values():
	print(str(number) + ' is a favorite')


