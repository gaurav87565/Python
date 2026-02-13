#Program Title : Calculating Simple Interest
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 13/02/2026       DOS :

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time: "))
simple_interest = (principal * rate * time) / 100
print("Interest =", simple_interest)