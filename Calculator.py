# This is a simple calculator program done in Python to learn the fundamentals

# Prints welcoming message, options for calculator, & choosing an option to perform
print("Hello there! Welcome to the Simple Calculator!")

print("1 - Add")
print("2- Subtract")
print("3 - Multiply")
print("4- Divide")

choice = int(input("Choose an operation:"))

if choice in [1,2,3,4]:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        result = num1 / num2

else:
    print("Invalid operation entered")

print(f"The result is {result}")