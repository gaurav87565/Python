#Program Title : Prime Number Analyzer*: Using function, write a Python program to analyze the input number is prime or not.
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 26/02/2026       DOS : 05/03/2026

def check_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))

if check_prime(n):
    print(n, "is a Prime Number.")
else:
    print(n, "is not a Prime Number.")