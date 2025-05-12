# Exercise 11
# Validate some user input (Use advanced string methods .isalpha, .isdigit, .find, also use len() function/method of python too, Make sure to use multpiple if else statement)

# 1. username must not be longer than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


username = input("Enter username: ")

length = len(username)
spaces = username.find(" ")
alpha = username.isalpha()


if length > 12:
    print(f"Length error: {length}")
elif spaces != -1:
    print(f"Spaces error")
elif alpha != True:
    print("Username cannot contain digits.")
else:
    print(f"Hello {username}!")