"""What are functions?"""
"""Functions are named blocks of code designed to do one specific job. Functions allow you to
write code once that can then be run whenever you need to accomplish the same task. Functions
can take in the information they need, and return the information they generate. Using functions
effectively makes your programs easier to write, read, test, and fix."""

"""Defining a function --> The first line of a function is its definition, marked by the keyword
'def'. The name of the function is followed by a set of parenthesis and a colon. A docstring, in
triple quotes, describes what the function does. The body of a function is indented one level. To
call a function, give the name of the function followed by a set of parenthesis."""


# Making a function
def greet_user():
	"""Display a simpple greeting."""
	print("Hello!")
	
	
greet_user()
print('**************************************************************')

"""Passing information to a function --> Information that's passed to a function is called an argument.
Information that's received by a function is called a parameter. Arguments are included in parenthesis
after the function's name, and parameters are listed in parenthesis in the function's definition."""


# Passing a single argument
def greet_user(name):
	"""Display a simple greeting."""
	print("Hello, " + name + "!")


greet_user('Paavan')
greet_user('Manju')
greet_user('Thilak')
print('************************************************************')


"""Positional and keyword arguments --> The two main kinds of arguments are positional
and keyword arguments. When you use positional arguments Python matches the first argument in the
function call with the first parameter in the function definition and so forth.
	With the keyword arguments, you specify which parameter each argument should be assigned to
in the function call. When you use keyword arguments, the order of the arguments doesn't matter."""


# Using positional arguments
def describe_pet(animal, name):
	"""Display information about a pet"""
	print(f'I have a {animal}.')
	print(f'It\'s name is {name}.')
	print('**********************************************************')


describe_pet('dog', 'crusoe')
describe_pet('fish', 'fighter')


# Using keyword arguments
def describe_pet(animal, name):
	"""Display information about a pet"""
	print(f'I have a cute {animal}.')
	print(f'It\'s nickname is {name}.')
	print('**********************************************************')
	

describe_pet(animal='Dog', name='Sony')
describe_pet(animal='Fish', name='Solomon')

"""Default Values --> You can provide a default value for a parameter. When function
calls omit this argument the default value will be used. Parameters with default values
must be listed after parameters without the default values in the function's definition
so positional arguments can still work correctly."""


# Using a default value
def describe_pets(name, animal='Dog'):
	"""Display information about a pet"""
	print(f'I have a {animal}.')
	print(f'It\'s name is {name}.')
	print('*************************************************************')


describe_pets('Bingo', 'Fish')
describe_pets('Romeo')


# Using None to make an argument optional
def describe_pets(animal, name=None):
	"""Display information about a pet"""
	print(f'I have a {animal}.')
	if name:
		print(f'It\'s name is {name}.')
		print('**************************************')


describe_pets('Dog')
describe_pets('Bird', 'Chirpieeee')

"""Return values --> A function can return a value or a set of values. When a
function returns a value, the calling line must provide a variable in which to store
the return value. A function stops running when it reaches a return statement."""


# Returning a single value
def get_full_name(first, last):
	"""Return a neatly formatted full name."""
	full_name = f'{first} {last}'
	return full_name


values = get_full_name('Paavan', 'Gopala')
print(f'My fullname is: {values}')
print('**********************************************************')


# Returning a dictionary
def build_person(first, last):
	"""Return a dictionary of information about a person."""
	person = {'first': first, 'last': last}
	return person


musician = build_person('A R', 'Rehman')
print(musician)


# Returning a dictionary with optional values
def build_person_1(first, last, age=None):
	"""Return a dictionary of information about a person."""
	person = {'first': first, 'last': last}
	if age:
		person['age'] = age
	return person


musician = build_person_1('Jimi', 'Hendrix', 27)
print(musician)

musician_1 = build_person_1('Janis', 'Joplin')
print(musician_1)
print('*********************************************************************')

"""Passing a list to a function --> You can pass a list as an argument to a function, and the
function can work with the values in the list. Any changes the function makes to the list will
affect the original list. You can prevent a function from modifying a list by passing a copy
of the list as an argument."""


# Passing a list as an argument.
def greet_user(names):
	"""print a simple greeting to everyone."""
	for name in names:
		print(f'Hello, {name}')


usernames = ['Paavan', 'Manju', 'Thilak']
greet_user(usernames)
print('*****************************************************************')


# Allowing function to modify the list
"""The following example sends a list of models to a function for
printing. The original list is emptied and the second list is filled."""
print(f'The original list is emptied and secondary list is filled. ')


def print_models(unprinted, printed):
	"""3D print a set of models"""
	while unprinted:
		current_model = unprinted.pop()
		print(f'Printing {current_model}')
		printed.append(current_model)
		

# Store some unprinted designs and print each one of them
unprinted = ['phone case', 'pendant', 'ring']
printed = []
print_models(unprinted, printed)

print(f'Unprinted {unprinted}')
print(f'Printed {printed}')
print('*****************************************************************')

# Preventing function to modify the list
"""The following example sends a list of models to a function for
printing. The original list is unchanged after calling print_models()."""
print(f'The original list is unchanged and new list is filled.')


def print_models(unprinted, printed):
	"""3D print a set of models"""
	while unprinted:
		current_models = unprinted.pop()
		print(f'Printing {current_models}')
		printed.append(current_models)
		

original = ['phone case', 'pendant', 'ring']
printed = []
print_models(original[:], printed)
print(f'Original: {original}')
print(f'Printed: {printed}')
print('**************************************************************')

"""Passing an arbitrary number of arguments --> Sometimes you won't know how many
arguments a function will need to accept. Python allows you to collect an arbitrary
number of arguments into one parameter using the *operator. A parameter that accepts
an arbitrary number of arguments must come last in the function definition.

The **operator allows a parameter to collect an arbitrary number of keyword arguments."""


# Collecting an arbitrary number of arguments
def make_pizza(size, *toppings):
	"""Make a pizza."""
	print(f'Making a {size} pizza.')
	print(f'Toppings:')
	for topping in toppings:
		print(f'- {topping}')


# Make three pizzas with different toppings
make_pizza('small', 'pepperoni')
print('*************************************************************')
make_pizza('large', 'bacon bits', 'pineapple')
print('*************************************************************')
make_pizza('medium', 'mushrooms', 'peppers', 'onions', 'extra cheese')
print('*************************************************************')


# Collecting an arbitrary number of keyword arguments
def build_profile(first, last, **user_info):
	"""Build a user's profile dictionary"""
	person = {'first': first, 'last': last}
	
	# Add any other keys and values.
	for key, value in user_info.items():
		person[key] = value
		
	return person


# Create two users with different kinds of information.
user_0 = build_profile('albert', 'einstein', location='priceton')
user_1 = build_profile('marie', 'curie', location='paris', field='chemistry')

print(user_0)
print(user_1)
print('*********************************************************************')

"""What's the best way to structure a function?"""
"""As you can see there are many ways to write and call a function. When you're starting out,
aim for something that simply works. As you gain experience you'll develop an understanding
of the more subtle advantages of different structures such as positional and keyword arguments,
and the various approaches to importing functions. For now if your funtions do what you need
them to do, you're doing well."""