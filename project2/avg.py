
counte = 0 
avg = 0
while True:
    score = input("please enter your score:")

    if score == "exit":
        break
    avg += float(score)
    counte += 1
    moadel = avg / counte

print(f"your averge : {moadel}")
    