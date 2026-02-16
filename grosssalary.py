#Program Title : Exploring Basic Arithmetic Operations in Python*: Write a Python program to explore basic arithmetic operations. The program should prompt the user to enter two numbers and then perform addition, subtraction, multiplication, division, and modulus operations on those numbers. The results of each operation should be displayed to the user.
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 12/02/2026       DOS : 19/02/2026

bs = float(input("Enter Basic Salary : "))
da = 0.70 * bs   # (70%)
ta = 0.30 * bs   # (30%)
hra = 0.10 * bs  # (10%)
gross_salary = bs + da + ta + hra

print("\nSalary Details:")
print("Basic Salary (BS):", bs)
print("Dearness Allowance (DA):", da)
print("Travel Allowance (TA):", ta)
print("House Rent Allowance (HRA):", hra)
print("Gross Salary:", gross_salary)
