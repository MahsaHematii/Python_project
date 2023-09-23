import random

computer_number = random.randint(1, 6)
print(computer_number)
while computer_number != 6:
    computer_number = random.randint(1, 6)
    print(computer_number)
    