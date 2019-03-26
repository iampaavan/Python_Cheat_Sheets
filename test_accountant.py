"""When it is okay to modify tests? --> In general you shouldn't modify a test once it's written.
When a test fails it usually means new code you've written has broken existing functionality, and
you need to modify the new code until all existing tests pass."""

import unittest
from Crash_Course.accountant import Accountant


class TestAccountant(unittest.TestCase):
	"""Test for the class Accountant"""
	def test_initial_balance(self):
		# Default balance should be 0.
		acc = Accountant()
		self.assertEqual(acc.balance, 0)
		
		# Test non-default balance.
		acc = Accountant(100)
		self.assertEqual(acc.balance, 100)
