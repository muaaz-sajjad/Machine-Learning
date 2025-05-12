# Exercise 9
# Python Weight Converter (Use multiple if else, typecasting concepts)

weight = float(input("Enter your weight: "))
unit = input("Which units are these?(K or P): ")

if unit == "K":
    weight = weight * 2.205
    print(f"The weight in pounds is {round(weight, 3)} lb.")
elif unit == "P":
    weight = weight / 2.205
    print(f"The weight in kilograms is {round(weight, 3)} kg.")
else:
    print(f"The unit '{unit}' is not valid!")