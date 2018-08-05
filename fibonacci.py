a = 0
b = 1
lasterm = 15
add = 0

print('Printing fibonacci series')
while add < lasterm:
	c = a + b
	print(str(c))
	a = b
	b = c
	c = a
	add += 1