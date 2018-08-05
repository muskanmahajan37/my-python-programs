def funTab():
	for i in range(1,8):
		print('# Table of ' + str(i))
		print('\n')
		for j in range(1,11):
			print(str(i) + " * " + str(j) + " = " + str(i*j))
		print('\n\n')


if 8 < 11:
	calling = funTab()
else:
	print("first number should be less than second number") 