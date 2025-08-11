#Ask user to input the length of the 3 sides of a triangle
x = float(input("Enter the first side:\n"))
y = float(input("Enter the second side:\n"))
z = float(input("Enter the third side:\n"))
# If all sides are equal, print equilateral
if x== y and y ==z:
    print("This is an equilateral triangle")
# If 2 sides are equal, print Isosceles
elif x==y or y==z or x==z:
    print("This is an isosceles triangle")
# If no sides are equal, print scelene
else:
    print("This is a scalene triangle")