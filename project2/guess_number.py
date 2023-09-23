import random

computer_number = random.randint(0 , 40)
Number_count = 0

while True:
    user_number = int(input("Please enter the number :"))
    Number_count += 1

    if computer_number == user_number:
        print("you win 🎉")
        print("The number of your guesses : " + str(Number_count))
        break
    
    
    elif computer_number > user_number:
        print("bro bala ⬆️")

    elif computer_number < user_number:
        print("bia paean ⬇️")

   