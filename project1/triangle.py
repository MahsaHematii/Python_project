a = float(input("Please enter the first number"))
b = float(input("Please enter the second number"))
c = float(input("Please enter the third number"))

if (c < a+b ) and (b < a+c) and (a < b+c):
    print("Yes")
else:
    print("No")