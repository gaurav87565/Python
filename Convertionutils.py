#Program Title : Developing Conversion Utilities
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 05/02/2026       DOS :

def rupee_to_dollar(rupees):
    rate = 90.58
    return rupees / rate

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def inch_to_feet(inches):
    return inches / 12

def main():
    print("--- Multi-Purpose Converter ---")
    print("1. Rupees to Dollars")
    print("2. Celsius to Fahrenheit")
    print("3. Inches to Feet")

    choice = input("\nSelect a conversion (1-3): ")

    if choice == '1':
        amt = float(input("Enter amount in Rupees: "))
        print(f"Result: ${rupee_to_dollar(amt):.2f}")

    elif choice == '2':
        temp = float(input("Enter temperature in Celsius: "))
        print(f"Result: {celsius_to_fahrenheit(temp):.2f}°F")

    elif choice == '3':
        inches = float(input("Enter length in inches: "))
        print(f"Result: {inch_to_feet(inches):.2f} feet")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()