n = int(input("please enter your number:"))

n1 = 1
n2 = 0
for i in range(n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
print(n3)