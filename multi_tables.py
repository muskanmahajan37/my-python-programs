def funTab():
	for i in range(1,n):
		print('# Table of ' + str(i))
		print('\n')
		for j in range(1,m):
			print(str(i) + " * " + str(j) + " = " + str(i*j))
		print('\n\n')

n = int(input('How many table you want? (This is the first number)'))
print(n, 'ok')
m = int(input('upto 10 or 20? (Second number)'))
print(m, 'glimpse at these')
if n < m:
	calling = funTab()
else:
	print("first number should be less than second number")