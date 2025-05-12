# logical operators = allow us to evaluate multiple conditions (or, not, and)
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition (not False, not True)

# temp = 25
# is_raining = False

# if temp > 30 or temp < 0 or is_raining:            ###### OR CONDITION
#     print("The outdoor event is cancelled!")
# else:
#     print("The outdoor event is schedueled!")


# temp = 20
# is_sunny = True
                                                                 #######   AND CONDITION
# if temp>=25 and is_sunny:
#     print("The outdoor event is cancelled!")
# else:
#     print("The outdoor event is schedueled!")



temp = 30
is_sunny = False
                                                                 ######   NOT CONDITION
if temp>=25 and not is_sunny:
    print("The outdoor event is cancelled!")
else:
    print("The outdoor event is schedueled!")



