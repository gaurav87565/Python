#Program Title : Triangle Pattern Generator Using Loops: Write a Python program to print a triangle pattern (give any), emphasizing the transition from C to Python syntax.
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 26/02/2026       DOS : 05/03/2026

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()