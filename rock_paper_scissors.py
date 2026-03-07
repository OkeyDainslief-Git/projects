import random


user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("type rock/paper/scissors or q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    # allow computer to pick any option (ties possible)
    computer_pick = random.choice(options)
    print("computer picked", computer_pick + ".")
    # handle tie case first
    if user_input == computer_pick:
        print("it's a tie! no points awarded.")
        continue

    if user_input == "rock" and computer_pick == "scissors":
        print("you win!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you win!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("you win!")
        user_wins += 1
        
    else:
        print("you lose!")
        computer_wins += 1


print("you won", user_wins, "times.")
print("the computer won", computer_wins, "times.")
print("goodbye!")

    





