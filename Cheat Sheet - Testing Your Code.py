"""Why test your code?"""

"""When you write a function or a class, you can also write tests for that code. Testing proves that your
code works as it's supposed to in the situations it's designed to handle, and also when people use your
programs in unexpected ways. Writing tests gives you confidence that your code will work correctly as more
people begin to use your programs. You can also add new features to your programs and know that you haven't
broken existing behavior."""

"""A unit test verifies that one specific aspect of your code works as it's supposed to. A test cae is a
collection of unit tests which verify your code's behavior in a whole variety of situations."""

"""Testing a function: A passing test --> Python's unittest module provides tools for testing your code.
To try it out, we'll create a function that returns a full name. We'll use the function in a regular program, and then
build a test case for the function."""


# A function to test
def get_full_name(first, last):
	"""Return a full name."""
	name = f'{first} {last}'
	return name


# Using the function
paavan = get_full_name('Paavan', 'Gopala')
print(paavan)

manju = get_full_name('Manjula', 'Subramanyam')
print(manju)
