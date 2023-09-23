# for i in range(4):
#     print("i am Mahsa")


# for i in range(3):
#     score_1 = float(input("Enter your Score:"))
#     print("thanks")
# print("the end")





# import math

# print("calculator")

# for i in range(40):


#     print("+ : Sum")
#     print("- : Squirting")
#     print("* : multiplication")
#     print("/ : Division")
#     print("sqrt")
#     print("sin")
#     print("cos")
#     print("tan")
#     print("cot")
#     print("fctorial")
#     print("Exit")

#     operation = input()

#     if operation == "Exit":
#         break

#     if operation == "+" or operation =="-" or operation ==  "*" or operation == "/":

#         Number_1 = float(input("Please enter the first number"))
#         Number_2 = float(input("Please enter the second number"))

#         if operation == "+":

#             print(Number_1 + Number_2)

#         elif operation == "-":
#             print(Number_1 - Number_2)

#         elif operation == "*":
#             print(Number_1 * Number_2)

#         elif operation == "/":
#             print(Number_1 / Number_2)

#     else:
#         a = float(input("Please enter the first number:"))

#         if operation == "sqrt":
#             print(math.sqrt(a))

#         elif operation == "sin":
#             b = math.radians(a)
#             print(math.sin(b))

#         elif operation == "cos":
#             b = math.radians(a)
#             print(math.cos(b))


#         elif operation == "tan":
#             b = math.radians(a)
#             print(1 / math.tan(b))

#         elif operation == "cot":
#             b = math.radians(a)
#             print(math.cot(b))

#         elif operation == "factorial":
#             print(math.factorial(a))


# for i in range(3):
#     password = input()
#     if password == "006600":
#         print("thats right ")
#         break
#     else:
#         print("wrong password")



    
import numpy as np
import pandas as pn
import matplotlib as plt

apple_width = np.random.normal(2,6,400)
apple_langth = np.random.normal(2,6,400)

plt.scatter(apple_width,apple_langth,color ="red")



