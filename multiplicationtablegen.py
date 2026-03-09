#Program Title : Multiplication Table Generator: Write a Python program to take a numerical input from the user and generate its multiplication table using loops.
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 26/02/2026       DOS : 05/03/2026

num = int(input("Enter a number: "))

print("\nMultiplication Table of", num)

for i in range(1, 11):
    print(num, "x", i, "=", num * i)