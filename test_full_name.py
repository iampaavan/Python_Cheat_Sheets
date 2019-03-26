import unittest
from Crash_Course.full_name import get_full_name


class NameTestCase(unittest.TestCase):
	"""Tests for full_name.py"""
	def test_first_last(self):
		"""Test names like Janis Joplin"""
		full_name = get_full_name('Janis', 'Joplin')
		self.assertEqual(full_name, 'Janis Joplin')

	def test_middle(self):
		"""Test names like David Lee Roth"""
		full_name = get_full_name('David', 'Roth', 'Lee')
		self.assertEqual(full_name, 'David Lee Roth')


if __name__ =="__main__()":
	unittest.main()


