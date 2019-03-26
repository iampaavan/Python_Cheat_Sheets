"""What are classes?"""
"""Classes are the foundation of object-oriented programming. Classes represent real-world
things you want to model in your programs: for example dogs, cars, and robots. You use a
class to make objects, which are specific instances of dogs, cars, and robots. A class
defines the general behavior that a whole category of objects can have, and the information
that can be associated with those objects."""

"""Classes can inherit from each other - you can write a class that extends the functionality
of an existing class. This allows you to code efficiently for a wide variety of situations."""

"""Creating and using a class --> Consider how we might model a car. What information would we
associate with a car, and what behavior would it have? The information is stored in variables
called attributes, and the behavior is represented by functions. Functions that are part of a
class are called methods"""


# The Car class
class Car():
	"""A simple attempt to model a car."""
	def __init__(self, make, model, year):
		"""Initialize car attributes."""
		self.make = make
		self.model = model
		self.year = year
		
		# Fuel capacity and level in gallons.
		self.fuel_capacity = 15
		self.fuel_level = 0
		
	def fill_tank(self):
		"""Fill gas tank to capacity"""
		self.fuel_level = self.fuel_capacity
		print(f'Fuel tank is full')

	def drive(self):
		"""Simulate driving"""
		print(f'The car is moving.')
	

# Creating an object from a class
my_car = Car('Audi', 'A4', 2016)

# Accessing the attributes
print('My car name is:', my_car.make)
print('My car model name is:', my_car.model)
print('My car manufacture year is:', my_car.year)

# Calling methods
my_car.fill_tank()
my_car.drive()

# Creating multiple objects
my_car_1 = Car('Lexus', 'FS-350', 2016)
my_car_1_old = Car('Subaru', 'Outback', 2013)
my_truck = Car('Toyota', 'Tacoma', 2010)

print('******************************************************************')

"""Modifying attributes --> You can modify an attribute's value directly, or you
can write methods that manage updating values more carefully."""
# Modifying an attribute directly
my_new_car = Car('Audi', 'A6', 2018)
print('My new car fuel level initially:', my_new_car.fuel_level)
my_new_car.fuel_level = 5
print(f'My new car fuel level after a while: {my_new_car.fuel_level}')


# Writing a method to update an attribute's value
def update_fuel_level(self, new_level):
	"""Update the fuel level."""
	if new_level <= self.fuel_capacity:
		self.fuel_level = new_level
	else:
		print(f'The tank can\'t hold that much.')


# Writing a method to increment an attribute's value
def add_fuel(self, amount):
	"""Add fuel to the tank."""
	if (self.fuel_level + amount) <= self.fuel_capacity:
		self.fuel_level += amount
		print('Added fuel.')
	else:
		print('The tank can\'t hold that much.')
		
		
print('--------------------------------------------------------------------')
"""Class Inheritance --> If the class you're writing is a specialized version of another class,
you can use inheritance. When one class inherits from another, it automatically takes on all the
attributes and methods of the parent class. The child class is free to introduce new attributes
and methods of the parent class.
To inherit from another class include the name of the parent class in parenthesis when defining
the new class."""


"""Instances as attributes --> A class can have objects as attributes. This allows classes
to work together to model complex situations."""


class battery():
	"""A battery for an electric car."""
	
	def __init__(self, size=70):
		"""Initialize the battery attributes"""
		# Capacity in kWh, charge level in %.
		self.size = size
		self.charge_level = 0
	
	def get_range(self):
		"""Return the battery's range"""
		if self.size == 70:
			return 240
		
		elif self.size == 85:
			return 270


# The __init__() method for a child class
class ElectricCar(Car):
	"""A simple model of an electric car."""
	def __init__(self, make, model, year):
		"""Initialize an electric car."""
		super().__init__(make, model, year)
		
		# Attribute specific to electric cars.
		self.battery = battery()
		# Battery capacity in kWh.
		self.batter_size = 70
		# Charge level in %
		self.charge_level = 0
		
	# Adding new methods to the child class
	def charge(self):
		"""Fully charge the vehicle"""
		self.charge_level = 100
		print(f'The vehicle is fully charged.')
		
	def fill_tank(self):
		"""Display an error message."""
		print(f'This car doesn\'t have fuel tank')
		

# Using child methods and parent methods
my_ecar = ElectricCar('Tesla', 'Model S', 2016)
my_ecar.charge()
my_ecar.drive()
my_ecar.fill_tank()

# Using an instance as an attribute
print(my_ecar.battery.get_range())
