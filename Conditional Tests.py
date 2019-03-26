bikes = ['trek', 'redline', 'giant']

if 'trek' in bikes:
	print()
	print('Element present in the list.')

else:
	print('Element not present. ')
print()

if 'surly' in bikes:
	print('Element present. ')
else:
	print('Element not present')
print()
print('******************************************')

user_input = int(input('Enter your age !!!'))

if user_input >= 18:
	print()
	print('You can vote!!')
else:
	print('Can\'t vote!')
	
print()
print('*******************************************')

user_input_1 = int(input('Enter you Age. '))

if user_input_1 < 4:
	ticket_price = 0
	print('Your ticket price is: ', ticket_price)
	
elif user_input_1 > 4 and user_input_1 < 18:
	ticket_price = 10
	print('Your ticket price is: {}'.format(ticket_price))
	
else:
	ticket_price = 15
	print(f'Your ticket price is: {ticket_price}')
	
print()
print('*******************************************')

for index, bike in enumerate(bikes, start=1):
	print(f'Index is: {index} and Bike name is: {bike}')
