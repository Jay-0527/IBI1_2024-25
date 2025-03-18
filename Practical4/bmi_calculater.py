#input height and weight
#calculate the result and output it
#output the health level
weight=float(input("Please write your weight here"))
height=float(input("Please write your height here")) #get your weight and height
BMI=weight/height**2 # cauculate it
if BMI>30:
    print(f"Your BMI is {BMI}, obese")
elif BMI<18.5:
    print(f"Your BMI is {BMI}, underweight")
else:
    print(f"Your BMI is {BMI}, normal state")