second = int(input("enter your second :"))
hours = second // 3600 
bor = (second - hours * 3600)
minutes = bor // 60
second_count = (bor - minutes * 60)%60
print(f"{hours}:{minutes}:{second_count}")