# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)
years = 90 - age_int
days = round(years * 365)
weeks = round(years * 52) 
months = round(years * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")


