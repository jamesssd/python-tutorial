# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# if year % 4 == 0 :
#     print("Leap Year")
# elif year % 100 == 0 :
#     print("Leap")
# elif year % 100 != 0 :
#     print("Not Leap")
# elif year % 400 ==0 :
#     print("Not Leap")
# elif year % 400 !=0 :
#     print("Not Leap")
# else : 
#     print("Fuck") 
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not leap year.")
    else :
        print("Leap year.")
else :
    print("Not Leap year.")