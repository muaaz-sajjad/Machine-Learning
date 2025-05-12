# indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step] ------ Syntax : remember "start" is inclusive and "end" is exclusive

credit_number = "1234-7689-2441-9203"
# result = credit_number[::] # prints whole string (from 0th to last index inluding all values, it does not exclude anything)
# result = credit_number[:5] # starts from index 0 (includes value at 0th index) & ends at index 5 (doesn't include value at index 5)
# result = credit_number[2:7] # starts from index 2 (includes value) and ends at index 7 (doesn't include value at 7)
# result = credit_number[::2] # prints everything from start to end with a step of 2 (it prints every 2nd value)
# result = credit_number[2:5:3] # prints every 3rd value from 2 (inclusive) to 5 (exclusive) index
# result = credit_number[-4:] # prints last 4 didgits
result = credit_number[::-1] # using negative step, it reverses the credit card number

print(result)