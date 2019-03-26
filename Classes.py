class Dog:
	"""Represent a Dog. """
	
	def __init__(self, name):
		self.name = name
		
	def sit(self):
		print(self.name + ' is sitting! ')


my_dog = Dog('Crusoe')

print(my_dog.name + " is a great dog. ")
my_dog.sit()
print()


# Inheritance
class SARDog(Dog):
	"""Represent a search dog. """
	
	def __init__(self, name):
		"""Initialize the sardog."""
		super().__init__(name)
		
	def search(self):
		"""Simulate searching"""
		print(self.name + ' is searching.')
		

my_dog_1 = SARDog('Willie')
print(my_dog_1.name + ' is a search dog.')
my_dog_1.sit()
my_dog_1.search()

