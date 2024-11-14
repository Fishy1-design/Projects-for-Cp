#ProficiencyTest: Rock, Paper, Scissors; Elisheva Kibbie

import random

def play_game():
    # these are the starting scores, they get displaied at the begining. I know, SHOCKING Σ(っ °Д °;)っ
    user_score = 0
    computer_score = 0
    
    options = ['rock', 'paper', 'scissors']

    # This is the main While loop🙀
    while True:
        # this displaies the current score
        print(f"Score: You - {user_score} | Computer - {computer_score}")
        
        # Ask the user for their choice, rock, paper, or scissors🪨📃✂️
        user_choice = input("Enter 'rock', 'paper', or 'scissors' (or 'quit' to stop the game): ").lower()

        # This gives the player an option to quit the game🙅‍♂️🙅‍♂️
        if user_choice == 'quit':
            print("Thanks for playing ╰（‵□′）╯!")
            break

        # Check if the user's choice is rock, paper, or scissors
        if user_choice not in options:
            print("Sorry, thats not an option, Did you spell your choice right?")
            continue  # Skip to the next part of the loop if there was an invalid input

        # this randomizes the computers choice. 
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # This determines who wins🤴
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # This re-starts the loop for another round.

if __name__ == "__main__":
    play_game()
