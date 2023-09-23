import random
x = 0
array = []
num = int(input("please  enter your number of array: "))

while len(array) < num:
    x = random.randint(0,num+1000)
    if x != array:
        array.append(x)

print(array)