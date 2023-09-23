user_list = []
revers_list = []

while True:
    user = input("please enter your number or enter exit : ")
    if user == "exit":
        break
    else:
        user_list.append(user)

for i in range(len(user_list),0, -1):
    revers_list.append(user_list[i-1])

print("your list =", user_list)
print("reverslist = ", revers_list)