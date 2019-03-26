"""Testing a class --> Testing a class is similar to testing a function, since you'll mostly
be testing your methods."""
# A class to test


class Accountant():
	"""Manage a bank account"""
	def __init__(self, balance=0):
		self.balance = balance
		
	def deposit(self, amount):
		self.balance += amount
		
	def withdraw(self, amount):
		self.balance -= amount
		
