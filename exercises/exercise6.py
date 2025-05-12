# Exercise 6 
# Calculating Hypotenous of a right angle triangle (hyp)² = (base)² + (altitude)²
# Use math.sqrt() typecasting, and f-string, and round() and pow(base, exponent)

import math

a = float(input("Enter Altitude of triangle: "))
b = float(input("Enter base of triangle: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"The hypotenous of the triangle is {c} cm.")
