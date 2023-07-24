rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
options = [rock, paper, scissors]

user_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(options[user_choice])

    computer_pick = random.randint(0,2)
    print("Computer chose: ")
    print(options[computer_pick])

    if user_choice == 0 and computer_pick == 1 :
        print(paper)
        print("Computer Wins")
    elif user_choice == 1 and computer_pick == 2 :
        print(scissors)
        print("Computer Wins")
    elif user_choice == 2 and computer_pick == 0 :
        print(rock)
        print("Computer Wins")
    elif computer_pick > user_choice:
        print("You lose")
    elif user_choice > computer_pick :
        print("You win")
    elif user_choice == computer_pick :
        print("Issa Draw")

    else : 
        print("You Win!")

