# Weight = float(input("enter your Weight:"))
# height = float(input("enter your height:"))

# r = round(height,2)

# BMI = Weight / (r*r)
# print(BMI)
# if BMI < 18.9:
#     print("Underweight")
# elif 18.5 <= BMI and BMI < 25:
#     print("Normal")
# elif BMI >= 25 and BMI < 30:
#     print("Overweight")
# elif BMI >= 30 and BMI <35 :
#     print("Obesity")

# elif BMI >= 35 and BMI < 40:
#         print("Extreme obesity")

n = float(input())
m = float(input())
r = round(m,2)
BMI = n / (m*m)
d = round(BMI,2) 
print(d)
if BMI < 18.9:
    print("Underweight")
    
elif 18.5 <= BMI < 25:
    print("Normal")

elif 25 <= BMI < 30:
    print("Overweight")

elif BMI >= 30 :
    print("Obese")

else:
    print("add eshtebah")