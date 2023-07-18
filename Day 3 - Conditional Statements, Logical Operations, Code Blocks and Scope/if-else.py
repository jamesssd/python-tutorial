print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you?"))
    if age >= 18 :
        bill = 12
        print("Adult tickets are $12")
    elif age >= 12 & age <= 18 : 
        bill = 5
        print("Child tickets are $5") 
    else :
        bill = 7
        print("Youth tickets are $7")
        
    pic = input("Do you want a photo taken? Y or N ")
    if pic == "Y" :
        bill += 3    
    
    print(f"Your final bill is ${bill}")
else :
    print("You cannot ride the rollercoaster! You have to grow before you ride this ride.")
    