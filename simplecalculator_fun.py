#Program Title : Simple Calculator Using Functions*: Implement a simple Python calculator that takes user input and performs basic arithmetic operations (addition, subtraction, multiplication, division) using functions.
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 26/02/2026       DOS : 05/03/2026

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero not allowed"

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice (1-4): "))

if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", subtract(num1, num2))
elif choice == 3:
    print("Result:", multiply(num1, num2))
elif choice == 4:
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")