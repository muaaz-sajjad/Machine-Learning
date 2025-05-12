# while loop = execute some code WHILE some condition remains true
# Logical operators are very useful in while loops
# While loops are essential for verifying some user inputs!




## Example 04  ##
num = int(input("enter a number b/w 1 and 10: "))

while num < 0 or num >10:
    print(f"number {num} is not valid!")
    num = int(input("enter a number b/w 1 and 10: "))
print(f"The number is {num}.")



## Example 3 ##
# age = int(input("enter age: "))

# while age < 0:
#     print(f"age cannot be negative!")
#     age = int(input("enter age: "))
# print(f"you are {age} years old.")




## Example 2 ##
# (not food == "e")  and (food != "e") both do the same job!

# food = input("enter food (e for exit): ")

# while food != "e":
#     print(f"You like {food}.")
#     food = input("enter food (e for exit): ")
# print("bye!")




## Example 1 ##
# age = int(input("enter age: "))

# while age < 18:
#     print(f"you are {age} years old. and you are NOT eligibile for vote!")
#     age = int(input("enter age: "))
# else:
#     print(f"you are {age} years old. and you are eligibile for vote!")

