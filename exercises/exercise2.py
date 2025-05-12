# Exercise 2
# Shopping Cart Program (use typecasting, input, f-string and variable concepts)

item = input("What item would you like to buy?: ")
price = float(input("What is the price of one item?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity


print(f"You bought {quantity} {item}/s.")
print(f"Your total bill is ${total}")
