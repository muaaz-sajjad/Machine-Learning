# conditional expression = a single one-line shortcut for the if-else statement (ternary operator)
# Print or assign one of the two values based on a condition
# X if condition else Y  -------- Formula
# 'X' and 'Y' can also be f-strings which is beautiful
# num = 5
# result = num % 2

# print("EVEN" if result == 0 else "ODD")

num = 5
a = 100
b = 300
age = 13
temperature = 20
user_role = "Guest"

# max_num = f"{a} is greater than {b}" if a>b else f"{b} is greater than {a}"
# min_num = f"{a} is smaller than {b}" if a<b else f"{b} is smaller than {a}" # f- string used in conditional expression (beautiful)
# status = f"You are adult because your age is {age} >= 18" if age >= 18 else f"You are a child because your age is {age} < 18"
# weather = "Hot" if temperature > 25 else "Not Hot"
access_level = f"Full Access because you are {user_role}." if user_role == "admin" else f"Limited access because you are {user_role}."

print(access_level)