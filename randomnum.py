num = int(input('Enter any random number (last number)\n'))
print(num)
mum = int(input('Enter another random number (to search)'))
print(mum)
for i in range(1,num):
	if mum == i:
		print('This number exists in the loop')
	else:
		print('Incorrect input')