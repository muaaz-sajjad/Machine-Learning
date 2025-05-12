# Advanced string methods, this is where we start rolling!
#        "string_variable is just a variable name, you can replace it with your variable!"
# string_variable.find("Anything first occurence of which we need! It can also be a space"), if we try to find something that is not there, it returns -1
# string_variable.rfind("Anything last occurence of which we need! It can also be a space"), if we try to find something that is not there, it returns -1
# string_variable.capitalize() ---It capitalizes first letter only (also it lower cases everything other than 1st letter, beautiful)
# string_variable.upper() ---It capitalizes all letters of a string
# string_variable.lower() ---It lower cases all the letters
# string_variable.isdigit() ---(Boolean) It gives True if all letters are digits without a space else gives a false
# string_variable.isalpha() ---(Boolean) It gives True if all letters are alphabets without a space else it gives a false
# string_variable.count("anything you need to count, a dash, a hash or a letter or even a number") ---It counts the number of given characters
#                                               Most useful methods
# string_variable.replace("Anything you want to replace", "The thing with which you are replacing")
#                                               For getting all string methods
# 

# name = input("Enter your name, I will find first 'b' in your name using 1st occurence method: ")
# name1 = input("Enter your name, I will find first occurence of anything in your name using 1st occurence method: ")
# search = input("Which charachter: ")
# result = name1.find(search)
# print(f"{search} is on number {result}, because in pyhton indexing starts from 0.")

# variable = input("Number: ")
# result = input("First Occurence letter: ")
# print(variable.rfind(result))

# number = "0312-0484192"
# result = "9"
# print(number.rfind(result))


# 


# print(help(str))

standard = float(input ("enter value you want to take mod of: "))
number = float(input("Enter num you want to take mod with: "))
result = number.__rmod__(standard)
print(result)
