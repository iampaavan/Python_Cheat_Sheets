# making a list
bikes = ['trek', 'redline', 'giant']

# get the first element in the list
print('First element in the list:', bikes[0])
print()

# get the second element in the list
print('Second element in the list:', bikes[1])
print()

# get the last element in the list
print('Last element in the list:', bikes[-1])
print()

# iterate through bikes list and print out the items one by one (using for loop)
for bike in bikes:
	print(bike)
print()

# iterate through the list and append it to another list
bikes_1 = []
for i in bikes:
	bikes_1.append(i)
print(bikes_1)
print()

# insert items to the list one by one by using append method
bikes_2 = []
print('Initial contents in the list:', bikes_2)
bikes_2.append('Pulsar')
bikes_2.append('CBR')
bikes_2.append('Honda')
print('After appending items to the list:', bikes_2)
print()

# making numerical lists
squares = []
for x in range(1, 11):
	squares.append(x**2)
print('List of squares from 1 to 10: ', squares)
print()

# list comprehension
squares_1 = [y * y for y in range(1, 11)]
print('List Comprehension, List of Perfect Squares: ', squares_1)
print()

# slicing a list
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
print('Get the first 2 items from the list: ', first_two)
print()

# copying to a new list from an existing list
copy_of_bikes = bikes[:]
print('Copy of bikes list to a new bikes list: ', copy_of_bikes)
print()



