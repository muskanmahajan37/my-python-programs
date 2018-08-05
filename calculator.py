def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
		return a * b

def divide(a, b):
	return a / b

def pow(a, b):
	return a ** b


	print('Select any of these by numbers')
	print('1. Addition\n')
	print('2. Subtraction\n')
	print('3. Multiplication\n')
	print('4. Division\n')
	print('5. power\n')

	select = int(input("1/2/3/4/5"))

	a = int(input('Enter first number'))
	b = int(input('Enter second number'))

	if select=='1':
 					print(a,' + ',b,' = ', add(a, b))
 					
 elif select=='2':
 					print(a,' - ',b,' = ', subtract(a, b))
 					
 elif select=='3':
 					print(a,' * ',b,' = ', multiply(a, b))
 					
 elif select=='4':
 					print(a,' / ',b,' = ', divide(a, b))
 					
 elif select=='5':
 					print(a,' ^ ',b,' = ', pow(a, b))