weight=int(input("enter your weight in pounds"))
height=int(input("Enter your height in inches"))
name=input("Enter your name")
BMI=(weight * 703)/(height * height)
print(BMI)
if BMI<18.5:
    print(name + " you are Underweight Minimal")
elif 18.5<BMI<24.9:
    print(name + " you are Normal Weight")
elif 25<BMI<29.9:
    print(name + " you are Overweight")
elif 30<BMI<34.9:
    print(name + " you are Obese")
elif 35<BMI<39.9:
    print(name + " you are severely obese")
else:
    print(name + " your weight is extremely high")
    
