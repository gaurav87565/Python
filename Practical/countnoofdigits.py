# Program to count number of digits

# Take input from user
num = input("Enter a number: ")

# Remove negative sign if present
if num.startswith('-'):
    num = num[1:]

# Count digits
digit_count = len(num)

# Display result
print("Number of digits:", digit_count)