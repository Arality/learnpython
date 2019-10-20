# Flow Control
#     Logic
#         if
#         Logical if, if the expression is true it will execute the code other wise it will be igrnored, see example
#         re
# if 5 == 10:
#     print(True)
# print(True)

#         else
#         Logical else, goes with if statments it tries first expression if it returns false it moves to this section
# if 5 == 10:
#     print(True)
# else:
#     print(False)

#         elif
#         Logical Else If, if the condition is not true for the first it will do this if the conditions are true
# x = 5
# if x == 10:
#     print("x = 10")
# elif x == 7:
#     print("x = 7")
# elif x == 5:
#     print("x = 5")
# else:
#     print("I don't know what x equals")

#     Loops
#         for
#         a for loop will iterate through the block of code while the expression is True, it has a self incrementing number
# listOfNames = ["Josh", "Lindsay", "Cash", "Ace", "Meatloaf"]
# for item in listOfNames:
#     print(item)

#         while
#         while loops will keep looping over the same code while an expression is True
x = 0
# while x < 10:
#     print(x)
#     x = x + 1

#     Control
#         break
#         to control the flow if we combine a loop with logic in case we want to break out of the loop entirely
# x = 0
# while x != 10:
#     x = x + 1
#     if x == 1:
#         print("x = 1")
#     elif x == 2:
#         print("x = 2")
#     elif x == 3:
#         print("x = 3")
#     elif x == 4:
#         print("x = 4")
#     elif x == 5:
#         print("x = 5")
#     elif x == 6:
#         print("x is above six, calling break")
#         break
#         x = 10
#     else:
#         print("Will we even print this?")

#         continue
#         Continue let's you bypass sections of code if you don't want to check them on the current iteration
# x = 1
# while x < 10:
#     if x == 5:
#         continue
#         x = 100
#     if x == type(int):
#         print(f"X is an integer {x}")
#         x = x + 1
    
    
#         pass
#         it is meant as a place holder for when you want to do things but haven't gotten around to writing them yet
# x = 0
# if x != 0:
#     pass
# print("Let's just skip the loop until we write it later")