#Program Title : Calculating Areas of Geometric figures
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 05/02/2026       DOS :

print("Welcome to Area Calculator")

def area_circle(radius):
    return 3.14159 * radius * radius

def area_rectangle(length, breadth):
    return length * breadth

def area_triangle(base, height):
    return 0.5 * base * height

print("\nChoose a geometric figure:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Enter your choice (1-3): ")

if choice == '1':
    r = float(input("Enter radius of the circle: "))
    print("Area of Circle =", area_circle(r))

elif choice == '2':
    l = float(input("Enter length of the rectangle: "))
    b = float(input("Enter breadth of the rectangle: "))
    print("Area of Rectangle =", area_rectangle(l, b))

elif choice == '3':
    base = float(input("Enter base of the triangle: "))
    height = float(input("Enter height of the triangle: "))
    print("Area of Triangle =", area_triangle(base, height))

else:
    print("Invalid choice!")