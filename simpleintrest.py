#Program Title : Calculating Simple Interest: Write a Python program to calculate the simple interest based on user input. The program should prompt the user to enter the principal amount, the rate of interest, and the time period in years. It should then compute the simple interest using the formula Simple Interest=(Principal×Rate×Time) /100  and display the result. 
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 12/02/2026       DOS :

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time: "))
simple_interest = (principal * rate * time) / 100
print("Interest =", simple_interest)