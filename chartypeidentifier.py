#Program Title : Character Type Identifier: Create a Python program to check whether the given input is a digit, lowercase character, uppercase character, or a special character using an 'ifelse-if' ladder.
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 26/02/2026       DOS : 05/03/2026

ch = input("Enter a character: ")

if ch.isdigit():
    print("It is a Digit.")
elif ch.islower():
    print("It is a Lowercase Character.")
elif ch.isupper():
    print("It is an Uppercase Character.")
else:
    print("It is a Special Character.")