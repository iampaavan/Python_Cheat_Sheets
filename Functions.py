# A simple function
def greet_user():
	"""Display a simple message"""
	print('Hello !')


greet_user()
print()


# Passing an argument
def greet_user(username):
	"""Display a personalized greeting"""
	print('Hello' + username + '!')


greet_user('Paavan')
print()


# Default values for parameters
def make_pizza(topping='Bacon'):
	"""Make a single-topping pizza"""
	print('Have a ' + topping + ' pizza!!!!')
	

make_pizza()
make_pizza('Pepperoni')
print()


# Returning a value
def add_numbers(x, y):
	"""Adding 2 numbers and returning the sum. """
	return x + y


print('Sum of two numbers are:', add_numbers(10, 5))


