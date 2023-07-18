# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
height_int = float(height)
weight_int = float(weight)

bmi = weight_int / (height_int * height_int)

if bmi < 18.5 :
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif bmi < 25 :
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif bmi < 30 :
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi < 40 :
    print(f"Your BMI is {round(bmi)}, you are obese.")
else :
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")

    
