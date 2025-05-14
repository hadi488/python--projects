import math

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Check if it's a quadratic equation
if a == 0:
    print("This is not a quadratic equation. 'a' cannot be 0.")
else:
    # Calculate the discriminant
    D = b ** 2 - 4 * a * c

    # Check the nature of the roots
    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"The equation has two distinct real roots: {root1} and {root2}")
    elif D == 0:
        root = -b / (2 * a)
        print(f"The equation has one real repeated root: {root}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-D) / (2 * a)
        print(f"The equation has two complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
