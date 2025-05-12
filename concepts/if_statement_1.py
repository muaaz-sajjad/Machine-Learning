# single '=' is for assignment
# double equal '==' is for comparison

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
elif response == "N":
    print("Okay, let me know when you need food!")
else:
    print("Choose either 'Y' or 'N'")
