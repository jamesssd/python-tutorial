#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

user_choice = input("Pick, heads? or tails?" )

flip_coin = random.randint(0,1)

if flip_coin == 0 :
    print("Tails")
else :
    print("Heads")
