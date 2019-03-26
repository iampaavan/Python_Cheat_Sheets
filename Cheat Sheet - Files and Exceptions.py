import json
"""What are files? What are exception?"""

"""Your programs can read information in from files, and they can write data to files.
Reading from files allows you to work with a wide variety of information; writing
to files allows users to pick up where they off the next time they run your programs.
You can write text to files, adn you can store Python structures as lists in data files."""

"""Exceptions --> Are special objects that help your programs respond to errors in appropriate
ways. For example if your program tries to open a file that doesn't exist, you can use exceptions to display
an informative error message instead of having the program crash."""

"""Reading from a file --> To read from a file your program needs to open the file and then read the
contents of the file at once, or read the file line by line. The 'with' statement makes sure the file is
closed properly when the program has finished accessing the file."""
print('*********************************************************************')

# Reading an entire file at once
filename = 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\sample.txt'
with open(filename, 'r') as file_read:
	contents = file_read.read()

print(contents)
print('*********************************************************************')

"""Reading line by line --> Each line that's read from the file has a newline character
at the end of the line, and the print function adds it's own newline character. The rstrip()
method gets rid of the extra blank lines and this would result in when printing to the terminal."""

file_name = 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\test_1.txt'
with open(file_name, 'r') as fileread:
	for line in fileread:
		print(line.rstrip())
print('*********************************************************************')

# Storing the lines in a list
f = 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\test_1.txt'
with open(f, 'r') as fr:
	lines_1 = fr.readlines()
	
for line_1 in lines_1:
	print(line_1.rstrip())
print('*********************************************************************')

"""Writing to a file --> Passing the 'w' argument to open() tells Python you want to
write to the file. Be careful; this will erase the contents of the file if it already exists.
Passing the 'a' argument tells Python you want to append to the end of an existing file."""
# Writing to an empty file.
write_file = 'write.txt'
with open(write_file, 'w') as wf:
	wf.write(f'I love programming!.\n')

# Writing multiple lines to an empty file
writer = 'write_1.txt'
with open(writer, 'w') as w:
	w.write(f'I love programming.\n')
	w.write(f'I love creating new games.\n')


# Appending to the file.
write_file_1 = 'write.txt'
with open(write_file_1, 'a') as write:
	write.write(f'I also love working with the data.\n')
	write.write(f'I love making apps as well.\n')


"""File paths --> When Python runs the open() function, it looks for the file in the same directory
where the program that's being executed is stored. You can open a file from a sub-folder using a
relative path. You can also use an absolute path to open any file on your system."""
# Opening a file from a sub-folder
file_reader = 'sub/reader.txt'
with open(file_reader, 'r') as read:
	lines = read.readlines()
	
for line in lines:
	print(line.rstrip())
print('*******************************************************************')

# Opening a file using an absolute path
f_path = 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\reader.txt'
with open(f_path, 'r') as fpath:
	liners = fpath.readlines()

for liner in liners:
	print(liner.rstrip())
print('********************************************************************')
f_path = 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\reader.txt'
with open(f_path, 'r') as fpath:
	liners = fpath.read()
	print(liners)
print('********************************************************************')

"""The try-except block --> When you think an error may occur, you can write a try-except
block to handle the exception that might be raised. The try blocks tells Python to try
running some code, and the except block tells Python what to do if the code results in
a particular kind of error."""

# Handling the ZeroDivisionError exception
try:
	print(5/0)
except ZeroDivisionError:
	print(f'You can\'t divide a number by 0')
print('********************************************************************')

# Handling the FileNotFoundError exception
try:
	with open('sub/f_name.txt') as f:
		f.read()
except FileNotFoundError:
	print(f'Can\'t find the file')
print('********************************************************************')

"""The else block --> The try block should only contain code that may cause an error.
Any code that depends on the try block running successfully should be placed in the else block."""
# Using an else block
print(f'Enter the two numbers. I\'ll divide them.')
x = input(f'First Number: ')
y = input(f'Second Number: ')

try:
	result = int(x) / int(y)
except ZeroDivisionError:
	print(f'You can\'t divide the number by 0. ')
except ValueError:
	print(f'Please enter integer values only.')
else:
	print(result)
print('*****************************************************************************************')

"""Preventing crashes from user input --> Without the except block in the following example, the program
would crash if the user tries to divide by zero. As written, it will handle the error gracefully and
keep running."""
"""A simple calculator for division only"""

print(f'Enter two numbers. I\'ll divide them.')
print(f'Enter q to quit.')

while True:
	x1 = input(f'Enter the first number:')
	if x1 == 'q':
		break
	y1 = input(f'Enter the second number:')
	if y1 == 'q':
		break
	try:
		result1 = int(x1) / int(y1)
	except ZeroDivisionError:
		print(f'Cannot divide the number by 0.')
	except ValueError:
		print(f'Please enter integers only.')
	else:
		print(result1)
print('*******************************************************************************')

"""Deciding which errors to report --> Well-written, properly tested code is not very prone to
internal errors such as syntax or logical errors. But every time your program depends on something external
such as user input or existence of a file, there's a possibility of an exception being raised."""

"""It's upto you how to communicate errors to your users. Sometimes users need to know if a file is
missing: sometimes it's better to handle the error silently. A little experience will help you know how much
to report."""

"""Failing silently --> Sometimes you want your programs to just continue running when it encounters an error,
without reporting the error to the user. Using the pass statement in an else block allows you to do this."""

# Using the pass statement in an else block
f_names = ['alice.txt', 'sidd.txt', 'write.txt', 'write_1.txt']
for f_name in f_names:
	# Report the length of each file found
	try:
		with open(f_name, 'r') as f_obj:
			lines = f_obj.readlines()
	except FileNotFoundError:
		pass
	else:
		num_lines = len(lines)
		print(f'{f_name} has {num_lines} lines. ')
print('************************************************************************************')

"""Avoid bare except blocks --> Exception-handling code should catch specific exceptions that you expect to happen
during your program's execution. A bare except block will catch all exceptions; including keyboard interrupts and
system exits you might need when forcing a program to close."""

"""If you want to use a try block and you're not sure which exception to catch, use Exception. It will catch most
exceptions, but still allow you to interrupt programs intentionally."""

# Don't use bare except blocks
try:
	# Do something
	print(10/0)
except:
	pass
# Use Exception instead
try:
	# Do something
	print(2/0)
except Exception:
	pass

# Printing the exception
try:
	print(5/0)
except Exception as e:
	print(e, type(e))

print('****************************************************************************')

"""Storing data with json --> The json module allows you to dump simple Python data structures into
a file, and load the data from that file the next time the program runs. The JSON data format is not
specific to Python, so you can share this kind of data with people who work in other languages as well."""

"""Knowing how to manage exceptions is important when working with stored data. You'll usually want to
make sure the data you're trying to load exists before working with it."""

# Using json.dump() to store data
numbers = [2, 3, 5, 7, 11, 13]
filename_1 = 'numbers.json'

with open(filename_1, 'w') as f_obj_json:
	json.dump(numbers, f_obj_json)
print('************************************************************')

# using json.load() to read data
"""Load some previously stored numbers."""
with open(filename_1, 'r') as f_read:
	obj_json = json.load(f_read)
print(obj_json)
print('*************************************************************')

# Making sure the stored data exists
try:
	with open(filename_1, 'r') as f_read_json:
		obj_json_1 = json.load(f_read_json)
except FileNotFoundError:
	print(f'Cannot find the file given.')
else:
	print(obj_json_1)
print('**************************************************************')
