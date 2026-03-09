#Program Title : Factorial Generator*: Design a Python program to compute the factorial of a given integer N.
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 26/02/2026       DOS : 05/03/2026

n = int(input("Enter a number: "))

fact = 1
for i in range(1, n + 1):
    fact = fact * i

print("Factorial of", n, "is", fact)