# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many spaces (fixed points) ---- f is for float
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate a positive value
# := = place sign to leftmost position
# :  = insert a space before positive numb ers
# :, = comma separatore for thousands

price1 =  30000.14159
price2 = -987000000.65
price3 = 1200000.34


## 8 ##
# using 3 flags togethore;        +        ,        .2f
print(f"Price 1 is: ${price1:+,.2f}")
print(f"Price 2 is: ${price2:+,.2f}")
print(f"Price 3 is: ${price3:+,.2f}")





## 7 ##
# this is a 1000 seperatore, it separates every 3 digits by comma
# print(f"Price 1 is: ${price1:,}")
# print(f"Price 2 is: ${price2:,}")
# print(f"Price 3 is: ${price3:,}")

## 06  ##
# adds positive sign to values which are positive
# print(f"Price 1 is: ${price1:+}")   
# print(f"Price 2 is: ${price2:+}")
# print(f"Price 3 is: ${price3:+}")


## 05  ##
# everything aligned perfectly even though we have a negative sign!
# print(f"Price 1 is: ${price1: }")   
# print(f"Price 2 is: ${price2: }")
# print(f"Price 3 is: ${price3: }")


## 04  ##
# It left justifies everyhting, it also the justification by default
# print(f"Price 1 is: ${price1:<}")
# print(f"Price 2 is: ${price2:<}")
# print(f"Price 3 is: ${price3:<}")

##   03  ##
# this is 0 padding, meaning it adds 10 numbers on left side of a number, such zeros have no value in reality (zeros on left are not important)
# print(f"Price 1 is: ${price1:010}")
# print(f"Price 2 is: ${price2:010}")
# print(f"Price 3 is: ${price3:010}")


##  02  ##
# using (.2f) puts 2 decimal places after the prices below, for e.g 3.14159 becomes 3.14, if (.3f) was used it would have become 3.141
# print(f"Price 1 is: ${price1:.2f}")
# print(f"Price 2 is: ${price2:.2f}")
# print(f"Price 3 is: ${price3:.2f}")

##  01  ##
# everything comes in 10 spaces after $ sign below (for example 12.34 carries a space of 4 digits/characters, using (12.34:10) adds 6 spaces before 12.34 and then writes 12.34 to make a total of 10 spaces
# print(f"Price 1 is: ${price1:10}")
# print(f"Price 2 is: ${price2:10}")
# print(f"Price 3 is: ${price3:10}")