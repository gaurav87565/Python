#Program Title : Number Type Identifier*: Develop a Python program that takes a numerical input and identifies whether it is even or odd, utilizing conditional statements and loops.
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 26/02/2026       DOS : 05/03/2026

num = int(input("Enter a number: "))

# Using conditional statement
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# Using a loop to check multiple numbers
choice = input("Do you want to check another number? (yes/no): ")

while choice.lower() == "yes":
    num = int(input("Enter another number: "))
    
    if num % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")
    
    choice = input("Check another number? (yes/no): ")

print("Program ended.")