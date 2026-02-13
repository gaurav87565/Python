#Program Title : Exploring Basic Arithmetic Operations in Python
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 13/02/2026       DOS :

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
print("\nSelect Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
choice = input("Enter your choice (1-7): ")
if choice == '1':
    print("Result:", a + b)
elif choice == '2':
    print("Result:", a - b)
elif choice == '3':
    print("Result:", a * b)
elif choice == '4':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error! Division by zero is not allowed.")
elif choice == '5':
    if b != 0:
        print("Result:", a % b)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid choice! Please select a number between 1 and 5.")
