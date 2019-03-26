"""List - A list stores a series of items in a particular order. Lists allow you
to store sets of information in one place, whether you have just a few items or
millions of items. Lists are one of the most powerful features readily accessible
to new programmers, and they tie together many important concepts in programming."""

# Making a list
users = ['val', 'bob', 'mia', 'ron', 'ned']

"""Individual elements in a list are accessed according to their position,
called the index."""
# getting the first element of the list
print(users[0])

# getting the second element of the list
print(users[1])

# getting the last element of the list
print(users[-1])

"""Once you've defined a list, you can change individual elements in the
list. You can do this by referring to the index of the item you want to
modify"""
# changing an element
print('List of items before changes:', users)
users[0] = 'valerie'
users[-2] = 'ronald'
print('**************************************************************')
print('List of items after changes:', users)
print('**************************************************************')

"""You can add elements to the end of a list, or you can insert them
wherever you want like in a list"""
# adding elements to the list
users.append('Paavan')
print(users)
print('**************************************************************')

# starting with an empty list
users_1 = []
users_1.append('Manju')
users_1.append('Paavan')
users_1.append('Thilak')
print('New list with new items:', users_1)
print('**************************************************************')

# insert elements at a particular position
users_1.insert(0, 'Sharu')
users_1.insert(4, 'Suuu')
print('List with newly inserted values:', users_1)
print('**************************************************************')

"""Removing elements - You can remove elements by their position in a list, or by
the value of the item."""
# deleting an element by it's position
del users_1[-1]
print('Deleted the last element of the list:', users_1)
print('**************************************************************')

# removing an item by it's value
users_1.remove('Sharu')
print('Deleted using the remove method, updated list is:', users_1)
print('**************************************************************')

"""Popping elements - if you want to work with an element that you're removing
from the list, you can "pop" the element. By default pop() returns the last element in
the list, but you can also pop elements from any position in the list"""

# pop the last item from a list
most_recent_user = users_1.pop()
print(most_recent_user)
print(users_1)
users_1.insert(2, 'Thilak')
print(users_1)
print('**************************************************************')

# Pop the first item in a list
first_user = users_1.pop(0)
print(first_user)
print(users_1)
print('**************************************************************')

"""List Length - The len() function returns the number of items in a list"""
num_users = len(users)
print(f'We have {num_users} users.')
print('**************************************************************')

users_1.append('Manju')
users_1.append('Suu')
users_1.append('Sharu')
print(users_1)
print('**************************************************************')

"""The sort() method changes the order of a list permanently. The
sorted() function returns a copy of the list, leaving the original list
 unchanged"""
# sorting a list permanently
users_1.sort()
print(users_1)
print('**************************************************************')

# sort the list permanently in reverse alphabetical order
users_1.sort(reverse=False)
print(users_1)
print('**************************************************************')

users_1.reverse()
print(users_1)
print('**************************************************************')

# sorting a list temporarily
print(sorted(users_1))
print('**************************************************************')

print(sorted(users_1, reverse=True))
print('**************************************************************')
print(users_1)

print()
users_1.sort()
print(users_1)
print('**************************************************************')

# Printing all the items in a list
for user in users_1:
	print(user)
print('**************************************************************')

# Printing a message for each item, and a separate message afterwards
for user in users_1:
	print(f'Welcome, {user} !')
print(f'Welcome, we\'re glad to see you all hear.')
print('**************************************************************')

"""You can use the range() function to work with a set of numbers efficiently. The range()
function starts at 0 by default, and stops one number below the number passed to it. You
can use the list() function to efficiently generate a large list of numbers"""
# printing the numbers 0 to 1000
for number in range(1001):
	print(number)
print('**************************************************************')
print()

# printing the numbers 1 to 1000
for n in range(1, 1001):
	print(n)
print('**************************************************************')
print()

# Making a list of numbers from 1 to a million
numbers = list(range(1, 1000000))
# print(numbers)
print('**************************************************************')
print()

"""There are a number of simple statistics you can run on a list
containing numerical data"""
# Finding the minimum value in a list
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)
print('The youngest member in the list is:', youngest)
print('**************************************************************')

# Finding the maximum value in a list
oldest = max(ages)
print('Oldest member of the list:', oldest)
print('**************************************************************')

# Finding the sum of all the values
print('Sum of all the values in the list:', sum(ages))
print('**************************************************************')

"""You can work with any set of elements from a list. A portion of a list is
called a slice. To slice a list start with the index of the first item you want,
then add a colon and index after the last item you want. Leave off the first index
to start at the beginning of the list, and leave off the last index to slice
through the end of the list"""
# Getting the first three items
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
print(finishers[:3])
print('**************************************************************')

# Getting the middle three items
print(finishers[1:4])
print('**************************************************************')

# Getting the last three items
print(finishers[-3:])
print('**************************************************************')

"""Copying a list - To copy a list make a slice that starts at the first item
and ends at the last item. If we try to copy a list without using this approach,
whatever you do to the copied list will affect the original list as well"""

# Making a copy of a list
copy_of_finishers = finishers[:]
print('Copy of finishers - List:', copy_of_finishers)
print('*************************************************************')

"""List Comprehension - You can use a loop to generate a list based on a range of
numbers or on another list. This is a common operation, so Python offers a more efficient
way to do it. List Comprehension may look complicated at first."""

squares = []
for s in range(1, 11):
	square = s ** 2
	squares.append(square)
print('Using common approach, the square of numbers from 1 to 10:', squares)
print('*************************************************************')

squares_1 = [s_1 ** 2 for s_1 in range(1, 11)]
print(f'Using the List Comprehension Approach: {squares_1}')
print('*************************************************************')

# Using a loop to convert a list of names to upper
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
print('List with it\'s items in lower case:', names)
print()
upper_names = []
for n in names:
	upper_names.append(n.upper())
print('List converted the items all to upper case:', upper_names)
print('************************************************************')

# Using the list comprehension to convert the list of names to upper case
names_1 = names[:]
print('Original List:', names_1)
print()

upper_names_1 = [name.upper() for name in names_1]
print(f'Using list comprehension, converted the list items to uppercase: {upper_names_1}')
print('************************************************************')

"""Tuples - A tuple is like a list, except you can\'t change the values in a tuple
once it\'s defined. Tuples are good for storing information that shouldn\'t be changed
throughout the life of a program. Tuples are designed by parenthesis instead of square
brackets. (You can overwrite an entire tuple, but can\'t change the individual elements
in a tuple)"""
# Defining a tuple
dimensions = (800, 600)
print('Original Tuple:', dimensions)
# Looping through the tuple
for dimension in dimensions:
	print(dimension)
dimensions = (1200, 900)
print('Overwritten the original Tuple:', dimensions)
print('********************************************************************')

"""Visualizing the Code - Build a list and print the items in the list"""
dogs = []
dogs.append('willie')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')

for dog in dogs:
	print(f'Hello {dog} !')
print(f'I love these dogs')

print('\nThese were my first two dogs:')
old_dogs = dogs[:2]
for old_dog in old_dogs:
	print(old_dog)

del dogs[0]
dogs.remove('peso')
print(dogs)
print('********************************************************************')
