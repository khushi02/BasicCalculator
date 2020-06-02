# Returns sum of x and y
def addition(x, y):
	return x+y

# Returns difference of x and y
def subtraction(x, y):
	return x-y

# Returns product of x and y
def multiplication(x, y):
	return x*y

# Returns division of x and y
def division(x, y):
	return x/y

# Returns x to the power of y
def exponents(x, y):
	return x**y

# Returns the remainder of x divided by y
def remainder(x, y):
	return x%y

# Print Table
print("Select Operation:")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. exponents")
print("6. remainder")
print("7. quit")

# Initialize running variable
running = True

# Run calculator
while running:
	choice = input("Enter choice (1, 2, 3, 4, 5, 6, 7): ")

	if choice in ('1', '2', '3', '4', '5', '6', '7'):
		if choice == '1':
			x = float(input("Enter first number: "))
			y = float(input("Enter second number: "))
			print(x, "+", y, "=", addition(x, y))
		elif choice == '2':
			x = float(input("Enter first number: "))
			y = float(input("Enter second number: "))
			print(x, "-", y, "=", subtraction(x, y))
		elif choice == '3':
			x = float(input("Enter first number: "))
			y = float(input("Enter second number: "))
			print(x, "x", y, "=", multiplication(x, y))
		elif choice == '4':
			x = float(input("Enter first number: "))
			y = float(input("Enter second number: "))
			print(x, "/", y, "=", division(x, y))
		elif choice == '5':
			x = float(input("Enter first number: "))
			y = float(input("Enter second number: "))
			print(x, "^", y, "=", exponents(x, y))
		elif choice == '6':
			x = float(input("Enter first number: "))
			y = float(input("Enter second number: "))
			print(x, "%", y, "=", remainder(x, y))
		elif choice == '7':
			running = False
	else:
		print("Please enter one of the 7 numbers.")
