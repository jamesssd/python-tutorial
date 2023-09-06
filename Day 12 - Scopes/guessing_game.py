"""Guess game
To do:
- create a game that has two option:
    - Easy Mode
    - 10 guesses to guess the number the computer is thinking
    
    -Hard Mode
    - 5 guess to guess the number the computer is thinking
    
"""
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
computer_guess = 12

is_player_correct = False

print("Welcome to the number guessing game!\nI'm thinking of a number between 1 to 100")
level = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
if level == 'easy':
    print("You have 10 guesses to guess the number!")
    life = 10
else:
    print("You have 5 guesses to guess the number")
    life = 5        

while not is_player_correct:
    user_guess = int(input("Make a guess: "))
    
    # def right_or_wrong():
    #     if user_guess != computer_guess:
    #         life -= 1
    #         return f"You have {life} remaining life left!"
    #         user_guess

    def check(user_guess):
        if user_guess == computer_guess:
            is_player_correct = True
            return f"You got it! The number is {computer_guess}"
            
        elif user_guess < computer_guess:
            #right_or_wrong()
            return "Too Low"
        else:
            #right_or_wrong()
            return "Too High"
            

    print(check(user_guess))

    