"""Dictionaries - Python's dictionaries allow you to connect pieces of related information.
Each piece of information in a dictionary is stored in a key-value pair. When you provide a
key, Python returns the value associated with that key. You can loop through all the
key-value pairs, all the keys, or all the values"""

# Making a dictionary
alien_0 = {'color': 'green', 'points': 5}

# Getting the value associated with the key
print(alien_0['color'])
print(alien_0['points'])
print('*************************************************')

# Getting the value with get()
alien_color = alien_0.get('color')
print('Color:', alien_color)
alien_points = alien_0.get('points')
print('Point\'s:', alien_points)
print('*************************************************')

# Adding a key-value pair
alien_0['x'] = 0
alien_0['y'] = 25
alien_0['speed'] = 1.5

print(alien_0)
print('*************************************************')

# Adding to an empty dictionary
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 10
print('Original value of alien_1:', alien_1)
print('*************************************************')

# Modifying values in a dictionary
alien_1['color'] = 'yellow'
alien_1['points'] = 15
print('Modified value of alien_1:', alien_1)
print('*************************************************')

# Deleting a key-value pair
del alien_0['x']
del alien_0['y']
print('Deleted few key-value pairs:', alien_0)
print('*************************************************')

"""Looping through a Dictionary - You can loop through a dictionary in three ways: you can
loop through all the key-value pairs; all the keys or all the values. A dictionary only tracks
connections between keys and values; it doesn't track the order of items in the dictionary;
if you want to process the information in order, you can sort the keys in your loop."""

# Looping through all the key-value pairs
# Storing people's favorite language
fav_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

# Show each person's favorite language
for name, language in fav_languages.items():
	print(name + ': ' + language)
print('************************************************************')

# Looping through all the keys - Show everyone who's taken the survey
for name in fav_languages.keys():
	print(name)
print('************************************************************')

# Looping through all the values - Show all the languages hat you have been chosen
for language in fav_languages.values():
	print(language)
print('************************************************************')

# Looping through all the keys in order - Show each person's favorite language
# in order by the person's name

for name in sorted(fav_languages.keys()):
	print(name + ': ' + fav_languages[name])
print('************************************************************')

"""Dictionary Length - You can find the number of key-value pairs in a dictionary"""
# Finding the dictionary's length
length = len(fav_languages)
print('Dictionary:', fav_languages)
print('Length of the dictionary:', length)
print('************************************************************')

"""Nesting - A list of dictionaries --> It's sometimes useful to store a set of
dictionaries in a list, this is called nesting."""
# Storing dictionaries in a list

# Start with an empty list
users = []

# Make a new user, and add them to the list
new_user = {
	'last': 'fermi',
	'first': 'enrico',
	'username': 'efermi'
}
users.append(new_user)

# Make another user, and add them to the list
new_user_1 = {
	'last': 'curie',
	'first': 'marie',
	'username': 'mcurie'
}
users.append(new_user_1)

# Show all the information about each user
for users_dict in users:
	for k, v in users_dict.items():
		print(k + ': ' + v)
	print('\n')
print('********************************************************')

"""You can also define a list of dictionaries directly, without using the append()"""
# Define a list of users, where each user is represented by a dictionary
print('Directly created dictionaries inside a list.')
users_1 = [
	{
		'last': 'fermi',
		'first': 'enrico',
		'username': 'efermi'
	},
	{
		'last': 'curie',
		'first': 'marie',
		'username': 'mcurie'
	}
]

for users_dict_1 in users_1:
	for k1, v1 in users_dict_1.items():
		print(k1 + ': ' + v1)
	print('\n')
print('*******************************************************')

"""Nesting - Lists in a dictionary --> Storing a list inside a dictionary
allows you to associate more than one value with each key"""
# Storing lists in a dictionary
# Store multiple languages in a dictionary

fav_languages_1 = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell']
}

# Show all responses for each person.
for n, l in fav_languages_1.items():
	print(n + ": ")
	for l1 in l:
		print("- " + l1)

print('***********************************************')

fav_languages_2 = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell']
}
# Show all responses for each person.
for n2, l2 in fav_languages_2.items():
	print('\n' + n2.title() + "\'s favorite languages are:")
	for l3 in l2:
		print("\t" + "-" + l3.title())

print('*************************************************************')

"""Nesting - A dictionary of dictionaries --> You can store a dictionary inside another
dictionary. In this case each value associated with a key is itself a dictionary"""

dicts = {
	'aeinstein': {
		'last': 'Albert',
		'first': 'Einstein',
		'location': 'Princeton'
	},
	'mcurie': {
		'last': 'Curie',
		'first': 'Marie',
		'location': 'Paris'
	}
}

for d1, d2 in dicts.items():
	print("\nUsername: " + d1)
	full_name = d2['first'] + " " + d2['last']
	# full_name += d2['last']
	location = d2['location']
	
	print("\tFullname: " + full_name)
	print("\tLocation: " + location)
print('***********************************************************')

"""Using an OrderedDict --> Standard Python dictionaries don't keep track of the order in
which keys and values are added; they only preserve the association between each key and it's value.
If you want to preserve the order in which keys and values are added, use an OrderedDict"""

# Preserving the order of keys and values

from collections import OrderedDict
favorite_languages = OrderedDict()

favorite_languages['jen'] = ['python', 'ruby']
favorite_languages['sarah'] = ['c']
favorite_languages['edward'] = ['ruby', 'go']
favorite_languages['phil'] = ['python', 'haskell']

print(favorite_languages)

# Display the results, in the same order they were entered

for n3, l4 in favorite_languages.items():
	print(n3 + ": ")
	for l5 in l4:
		print("- " + l5)
print('***********************************************************')

"""Generating a million dictionaries --> You can use a loop to generate a large
number of dictionaries efficiently, if all the dictionaries start out with
same or similar data."""

aliens = []

for alien_num in range(1000000):
	new_alien = {}
	new_alien['color'] = 'green'
	new_alien['points'] = 5
	new_alien['x'] = 20 * alien_num
	new_alien['y'] = 0
	aliens.append(new_alien)
	
# Prove the list contains a million aliens
num_aliens = len(aliens)

print(f'Number of aliens created: {num_aliens}')
print('***************************************************************')
