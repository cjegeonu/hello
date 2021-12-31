import random # this imports the randm library

user_wins = 0 # this is the user wins variable
computer_wins = 0 # this is the computer wins variable

options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_input == "q":
        print("Goodbye!")
        break

    if user_input == "score":
        print("You won",user_wins,"times. The computer won",computer_wins,"times.")
        continue

    if user_input == "help":
        print("Type rock, paper, or scissors to play the game, score to see the score, and q to quit.")
        continue

    if user_input not in options:
        print('Unknown command. Type "help" for help.')
        continue

    random_number = random.randint(0,2)
    # rock is 0, paper is 1, and scissors is 2
    computer_input = options[random_number]
    print("The computer picked", computer_input + ".")

# user win conditioons
    if user_input == "rock" and computer_input == "scissors":
        print("You won!")
        user_wins += 1
        print("You won",user_wins,"times. The computer won",computer_wins,"times.")
        continue
    
    if user_input == "paper" and computer_input == "rock":
        print("You won!")
        user_wins += 1
        print("You won",user_wins,"times. The computer won",computer_wins,"times.")
        continue

    if user_input == "scissors" and computer_input == "paper":
        print("You won!")
        user_wins += 1
        print("You won",user_wins,"times. The computer won",computer_wins,"times.")
        continue

#computer win conditions
    if user_input == "rock" and computer_input == "paper":
        print("Computer won!")
        computer_wins += 1
        continue
    
    if user_input == "paper" and computer_input == "scissors":
        print("Computer won!")
        computer_wins += 1
        continue

    if user_input == "scissors" and computer_input == "rock":
        print("Computer won!")
        computer_wins += 1
        continue

#tie conditions
    if user_input == "rock" and computer_input == "rock":
        print("You tied.")
        continue
    
    if user_input == "paper" and computer_input == "paper":
        print("You tied.")
        continue

    #modification

    if user_input == "scissors" and computer_input == "scissors":
        print("You tied.")
        continue
