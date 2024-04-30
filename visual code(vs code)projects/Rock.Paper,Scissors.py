import random
options = ("rock","paper","scissors")
player = None
computer = random.choice(options)

while player not in options:
 player = input("Enter a choice (rock,paper,scissors):")

print(f"Player:{player}")
print(f"Computer:{computer}")

if player == computer:
  print("It's a tie!")
  print("Thanks for playing! ") 
elif player == "rock" and computer == "scissors":
  print("You Win!")
  print("Thanks for playing! ") 
elif player == "paper" and computer == "rock":
  print("You Win!") 
  print("Thanks for playing! ") 
elif player == "scissors " and computer == "paper ":
  print("You Win!") 
  print("Thanks for playing! ") 
else:
  print("You lose!")
  print("Thanks for playing! ")   
