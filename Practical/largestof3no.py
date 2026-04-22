# Program to find largest and smallest number

# Take three numbers as input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Find largest
largest = max(a, b, c)

# Find smallest
smallest = min(a, b, c)

# Display result
print("Largest number:", largest)
print("Smallest number:", smallest)