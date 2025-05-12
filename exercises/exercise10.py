# Exercise 10
# Temperature Conversion Program (Use Typecasting, multiple if else concepts)

unit = input("Is this temperature in Celcius or Farnheit (C/F)?: ")
temp = float(input("Enter the temperatue: "))

if unit == "C":
    temp = ((temp * (9/5)) + 32)
    print(f"The temperature in Farnheit is {round(temp, 2)} °F.")
elif unit == "F":
    temp = ((temp - 32) * (5/9))
    print(f"The temperature in Degree Celcius is {round(temp, 2)} °C.")
else:
    print(f"{unit} is not a valid unit!")


