# Calculating circumference of a circle 2(pi)r
# Use built-in math module math.pi, typecasting, and f-string, and round()

import math
radius = float(input("enter the radius of a circle: "))
circum = 2 * math.pi * radius

print(f"The circumferenc of the circle is {round(circum, 2)} cm.")