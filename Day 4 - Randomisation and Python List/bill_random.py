# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

import random

#Write your code below this line 👇

# random_names = random.choice(names)

# print(f"{random_names} is going to buy the meal today!")

#Without using choice
num_items = len(names)

random_choice = random.randint(0, num_items-1)
winner = names[random_choice]

print(winner + " is going to buy the meal today!")