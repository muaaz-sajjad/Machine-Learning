# Exericise 5
# Calculating the area of a circle (pi)r²
# Use built-in math module math.pi, typecasting, and f-string, and round() and pow(base, exponent)

import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius,2)

print(f"The area of the circle is {round(area, 3)} cm²")