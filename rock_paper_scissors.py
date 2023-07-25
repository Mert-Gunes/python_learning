import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the rock, paper and scissors game!")
move = int(input("Select a move to make. Type 0 for rock, 1 for paper and 2 for scissors."))
moves = [rock, paper, scissors]

computers_move = random.randint(0,2)

print("Your move is")
if move == 0:
    print(rock)
elif move == 1:
    print(paper)
else:
    print(scissors)

print("computer's move is")
if computers_move == 0:
    print(rock)
elif computers_move == 1:
    print(paper)
else:
    print(scissors)

if move == 0:
    if computers_move == 0:
        print("it's a draw.")
    elif computers_move == 1:
        print("You lose.")
    else:
        print("you win!") 
elif move == 1:
    if computers_move == 1:
        print("it's a draw.")
    elif computers_move == 2:
        print("You lose.")
    else:
        print("you win!") 
else:
    if computers_move == 2:
        print("it's a draw.")
    elif computers_move == 1:
        print("You lose.")
    else:
        print("you win!") 