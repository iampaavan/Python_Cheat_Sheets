# A simple while Loop

current_value = 1

while current_value <= 5:
	print(current_value)
	current_value += 1

print()
print('***************************************')
print()

# Letting the user choose when to quit

msg = ''
while msg != 'quit' and 'Quit' and 'QUIT':
	msg = input('What\'s your message? ')
	print(msg)


