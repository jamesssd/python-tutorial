print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you?"))
    if age >= 18 :
        print("The price for the tickets is $12")
    elif age >= 12 & age <= 18 : 
        print("The price for the ticket is $5") 
    else :
        print("The price for the tickets is $7")
else :
    print("You cannot ride the rollercoaster! You have to grow before you ride this ride.")
    