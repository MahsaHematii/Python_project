
Number1 = int(input("please enter your first Number: "))
Number2 = int(input("please enter your second Number: "))
Bmm = 0

if Number1 > Number2:
    Kmm = Number2

elif Number1 < Number2:
    Kmm = Number1

for i in range(1 , Kmm+1):
    if Number1 % i == 0 and Number2 % i == 0:
        Bmm = i
Kmm = (Number1 * Number2)/Bmm
print(f"Kmm : {Kmm}")