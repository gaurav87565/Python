#Program Title : Calculating Gross Salary of an Employee*: Write a Python program to calculate thegross salary of an employee. The program should prompt the user for the basic salary(BS) and then compute the dearness allowance (DA) as 70% of BS, the travel allowance(TA) as 30% of BS, and the house rent allowance (HRA) as 10% of BS. Finally, it shouldcalculate the gross salary as the sum of BS, DA, TA, and HRA and display the result.
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