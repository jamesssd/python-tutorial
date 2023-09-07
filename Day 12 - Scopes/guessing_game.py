from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

is_game_off = False

turns = 0
def check(user_guess, computer_guess, turns):
        """checks to see if user_guess is the same as computer guess Returns the number of turns remaining"""
        if user_guess == computer_guess:
            print(f"You got it! The number is {computer_guess}")
            if input("Do you want to play again? Type 'y': ") == 'y':
                game()
            else:
                print("Have a great day!")
        elif user_guess < computer_guess:
            print("Too Low")
            return turns -1
        else:
            print("Too High")
            return turns -1

computer_guess = randint(1,100)

def difficulty():
    level = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():   
    print(logo)     
    print("Welcome to the number guessing game!\nI'm thinking of a number between 1 to 100")

    turns = difficulty()

    user_guess = 0
    while user_guess != computer_guess:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        user_guess = int(input("Make a guess: "))
        
        turns = check(user_guess, computer_guess, turns)
        if turns == 0:
            return "You've run out of guesses, you lose!"
        elif user_guess != computer_guess:
            print("Guess again")
            
game()
        