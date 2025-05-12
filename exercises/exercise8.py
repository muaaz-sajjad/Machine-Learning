# Exercis 8: Calculator Program
# Use typecasting, algebraic operators, and multiple else if statements


operator = input("Enter and operator (+, -, *, /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1+num2
    print(round(result, 2))
elif operator == "-":
    result = num1-num2
    print(round(result, 2))
elif operator == "*":
    result = num1*num2
    print(round(result, 2))
elif operator == "/":
    result = num1/num2
    print(round(result, 2))
else:
    print(f"You selected a wrong operator '{operator}'!")