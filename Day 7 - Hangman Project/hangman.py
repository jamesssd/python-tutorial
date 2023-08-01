# #Step 1 

# word_list = ["aardvark", "baboon", "camel"]

# import random

# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# word = random.choice(word_list)
# random_word = list(word)
# print(random_word)
# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter: ").lower()
# print(guess)
# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# for letter in random_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("wrong")

#Step 2

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #TODO-1: - Create an empty List called display.
# #For each letter in the chosen_word, add a "_" to 'display'.
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# guess = input("Guess a letter: ").lower()
# display=[]
# len_word = len(chosen_word)
# for _ in range(len_word):
#     display.append("_")
# print(display)
# #TODO-2: - Loop through each position in the chosen_word;
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# for position in range(len_word):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter

# #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# print(display)

#Step 3 & 4

import random
import hangman_words
import hangman_art

print(hangman_art.logo)

art = hangman_art.stages

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False
live = 6
while not end_of_game:  
    guess = input("Guess a letter: ").lower()
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(art[live])
    if guess not in chosen_word:
        live -= 1
        print(art[live])
        if live == 0:
            end_of_game=True
            print("You lost!")
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("Game is over, you won!")
    
    # print(display)
    
    