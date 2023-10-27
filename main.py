
import random

options = ["rock", "paper", "scissors"]
# emoji = {}


choice = input("Enter your choice from rock,paper and scissors\n")
computer = random.choice(options)

print(choice, computer)

if choice == computer:
    print("Tie!")
elif (choice == "rock" and computer == "scissor")  or (choice == "paper" and computer == "rock") or (choice == "scissor" and computer == "paper") :
    print("User Won!")
else :
    print("Computer Won!")


