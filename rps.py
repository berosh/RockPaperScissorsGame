import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

print("Let\'s play Rock, Paper and Scissors")

playerchoice = input("Enter... \n1 for Rock\n2 for Paper\n3 for Scissor\n\n")
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You enter a wrong choice. Try again!")

computerchoice = random.choice("123")
computer = int(computerchoice)  

print("You choose " + str(RPS(player)).replace("RPS." , "") + ".") 
print("Computer choose " + str(RPS(computer)).replace("RPS." , "") + ".") 

if player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
elif player == computer:
    print("Tie game!")
else:
    print("Computer wins!")


    

