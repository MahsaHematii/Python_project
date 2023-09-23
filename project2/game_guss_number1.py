import random

computer_number = random.randint(10, 40)
count_name = 0

while True:
    user_number = int(input())
    count_name += 1


    if computer_number == user_number:
        print("you win")
        print("😁💪")
        print("youuuuuuu wiiiiiiiiin" + str (count_name))
        break

    elif computer_number < user_number:
        print("bia payiin")

    elif computer_number > user_number:
        print("get up")
        
    