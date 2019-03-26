# reading a file and storing it's lines
filename = 'paavan.txt'

with open('paavan.txt', 'r') as file_read:
	lines = file_read.readlines()
	
for line in lines:
	print(line)


# Writing to a file
filename_1 = 'sample.txt'

with open('sample.txt', 'w') as file_write:
	file_write.write('I love programming.')

# Appending to a existing file

with open('sample.txt', 'a') as file_write:
	file_write.write("\nI love making games. ")
