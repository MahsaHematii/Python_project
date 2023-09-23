import math

number = int(input("please enter your number: "))

x = 1
factorial = 1

while True:
    factorial = factorial * x
    x += 1
    factorial *= x

    if factorial == number:
        print("ok, good")

    else:
        print("no")