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
selection = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
user_choice = int(input("What do you choose? Type 0 for Rock, "
                   "1 for Paper or 2 for Scissors.\n"))

print(selection[user_choice])

print("Computer Chooses:")
print(selection[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice ==2:
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print("You loose")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice > user_choice:
    print("You loose")
elif user_choice == computer_choice:
    print("It's a draw")


