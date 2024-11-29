# Rock Paper Scissors ASCII Art
# Rock beats scissor
# Scissors beat paper
# Paper beat rock
# Rock
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
userInput = int(input("Enter your choice 0 for ROCK, 1 for PAPER and 2 for SCISSOR\n"))

computerInput = -1
if 3 > userInput >= 0:
    computerInput = random.randint(0,2)
    print(game_images[computerInput])
    if userInput == computerInput:
        print("Draw")
    elif userInput == 0 and computerInput == 2:
        print ("You win")
    elif userInput == 2 and computerInput == 0:
        print("You Win")
    elif userInput > computerInput:
        print("You win")
    elif computerInput > userInput:
        print("You loose")

else:
    print("Entered values is invalid")


