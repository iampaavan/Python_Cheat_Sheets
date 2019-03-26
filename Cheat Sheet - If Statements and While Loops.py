"""What are if statements? What are while loops?"""

"""If statements allow you to examine the current state of a program
and respond appropriately to that state. You can write a simple if
statement that checks one condition, or you can create a complex series
of if statements that identify the exact conditions you're looking for."""

"""While loops run as long as certain conditions remain true. You can use while
loops to let your programs run as your users want them to."""

"""Checking for equality --> A single equal sign assigns a value to a variable.
A double equal sign (==) checks whether two values are equal."""

car = 'bmw'
print('Checking inequality', car == 'bmw')

car = 'audi'
print('Checking inequality', car == 'bmw')

# Ignoring case when making a comparison
car = 'Audi'
print('Ignoring case when making a comparison:', car.lower() == 'audi')

# Checking inequality
topping = 'mushrooms'
print('Checking inequality:', topping != 'anchovies')
print('***********************************************************************')

"""Numerical comparisons --> Testing numerical values is similar to testing
string values."""
# Testing equality and inequality
age = 18
print('Testing Equality:', age == 18)

print('Testing Inequality:', age != 18)

# Comparison Operators
my_age = 27
print('My age is less than 21:', my_age < 21)
print('My age is greater than 21:', my_age > 21)
print('My age is greater than equal to 21:', my_age >= 21)

"""Checking multiple conditions --> You can check multiple conditions at the same time.
The 'and' operator returns 'True' if all the conditions listed are 'True'. The 'or' operator
returns 'True' if any condition is 'True'. """

age_0 = 22
age_1 = 18

print('Checking multiple conditions with "and" operator:', age_0 >= 21 and age_1 >= 21)

age_1 = 23
print('Checking multiple conditions with "and" operator:', age_0 >= 21 and age_1 >= 21)

# Using 'or' to check multiple conditions
age_0 = 22
age_1 = 18
print('Checking multiple conditions with "or" operator:', age_0 >= 21 or age_1 >= 21)
age_0 = 18
print('Checking multiple conditions with "or" operator:', age_0 >= 21 or age_1 >= 21)

"""Boolean values --> A boolean value is either True or False. Variables with boolean
values are often used to keep track of certain conditions within a program."""
# Simple boolean values
game_active = True
can_edit = False

"""If statements --> Several kinds of if statements exist. Your choice of which to use
depends on the number of conditions you need to test. You can have as many elif blocks
as you need, and the else block is always optional."""
# Simple if statement
age = 19
if age >= 18:
	print('You\'re old enough to vote.')
print('************************************************************')

# if-else statements
age = 17
if age >= 18:
	print('You\'re old enough to vote.')
else:
	print('You can\'t vote yet.')
print('************************************************************')

# The if-elif-else chain
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10

print(f'Your cost is $:{str(price)}')
print('************************************************************')


"""Conditional tests with lists --> You can easily test whether a certain value is in a list.
You can also test whether a list is empty before trying to loop through the list"""

players = ['al', 'bea', 'cyn', 'dale']
test = 'al' in players
print('Value is present in the list:', test)

test = 'eric' in players
print('Value present in the list:', test)
print('************************************************************')

# Testing if a value is not in a list
banned_users = ['ann', 'chad', 'dee']
user = 'erin'

if user not in banned_users:
	print('You can play!')
print('********************************************************')

# Checking if a list is empty
players = []

if players:
	for player in players:
		print("Player:" + player.title())
else:
	print('We have no players.')
print('*********************************************************')

"""Accepting input --> You can allow your users to enter input using the
input() statement in Python 3, all the input is stored as a string."""
# Simple input
name = input('What\'s your name?')
print('Hello, ' + name + '.')

# Accepting numerical input
age = input('How old are you? ')
age = int(age)

if age >= 18:
	print('You can vote!')
else:
	print('You can\'t vote yet.')
print('*******************************************************')


"""While loops --> A while loop repeats a block of code as long as
a condition is 'True'. """
current_value = 1

while current_value <= 5:
	print(current_value)
	current_value += 1
print('*******************************************************')

# Letting the user choose when to quit
prompt = "Tell me something, and I'll "
prompt += "repeat it back to you."
prompt += "\nEnter 'quit' to end the program."

msg = ""
while msg != 'quit':
	msg = input(prompt)
	
	if msg != 'quit':
		print(msg)
print('********************************************************')

# Using a flag
prompt = "Tell me something, and I'll "
prompt += "repeat it back to you."
prompt += "\nEnter 'quit' to end the program."

active = True
msg = ""
while active:
	msg = input(prompt)

	if msg == 'quit':
		active = False
	else:
		print(msg)

print('*******************************************************')
# Using break to exit a loop
prompt = "What cities have you visited?"
prompt += "\nEnter 'quit' when you are done."

while True:
	city = input(prompt)
	
	if city == 'quit':
		break
	else:
		print(city)

# Breaking out of loops
"""You can use the break statement and the continue statement with any of Python's loops.
For example you can use 'break' to quit a 'for' loop working through the list or a dictionary.
You can use 'continue' to skip over certain items when looping through a list or dictionary as well"""

# Using continue in a loop
banned_users = ['eve', 'fred', 'gary', 'helen']

prompt = "Add a player to your team"
prompt += "\nEnter 'quit' when're done. "

players = []
while True:
	player = input(prompt)
	if player == 'quit':
		break
	elif player in banned_users:
		continue
	else:
		players.append(player)
print("\nYour team:")
for player in players:
	print(player)
print("Your team members:", list(players))
print('*********************************************************')

"""Avoiding infinite loops --> Every while loop needs a way to stop running so it won't
continue to run forever. If there's no way for the condition to become False, the loop
will never stop running"""

while True:
	name = input("What's your name?")
	if name == 'quit':
		break
	print("Nice to meet you, " + name)

"""Removing all instances of a value from a list"""
"""The remove() method removes a specific value from a list, but it only removes
the first instance of the value you provide. You can use a while loop to remove all
instances pf a particular value"""

pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print("Original pets list with few duplicates:", pets)

while 'cat' and 'dog' in pets:
	pets.remove('cat')
	pets.remove('dog')

print("Refined pets list without duplicates:", pets)
