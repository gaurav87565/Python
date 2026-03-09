#Program Title : Fibonacci Sequence Generator: Develop a Python program to print the Fibonacci sequence using a while loop.
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 26/02/2026       DOS : 05/03/2026

n = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

print("Fibonacci Sequence:")

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1