Name = input("please enter your name : ")
family = input("please enter your family : ")
lesson_1 = input("please enter your frist Score : ")
lesson_2 = input("please enter your second Score : ")
lesson_3 = input("please enter your third Score : ")

Avg = (lesson_1 + lesson_2 + lesson_3)/3

if Avg >= 17:
    print("Great")

elif Avg <= 12 or Avg < 17:
    print("Normal")

elif Avg <12:
    print("Fail")