Number1 = int(input("please enter your first Number: "))
Number2 = int(input("please enter your second Number: "))

if Number1 > Number2:
    Bmm = Number1

elif Number1 < Number2:
    Bmm = Number2

for i in range(1, Bmm + 1):
    if Number1 % i == 0 and Number2 % i == 0:
        print(f"Bmm : {i}")

