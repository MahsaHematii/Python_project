number = int(input("please enter lenght your list :  "))
list = []
list2 = []

for i in range(number):
    x = (int(input("plese enter your number: ")))

print(list)

for x in list:
    if x not in list2:
        list2.append(x)

print(list2)