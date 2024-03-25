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
pool = [rock, paper, scissors]
while True:
    choice = int(input ("What do you choose? 1 for Rock, 2 for Paper, 3 for Scissors. "))
    
    if choice in (1,2,3):
        print(pool[choice-1])
        comp_choice = random.randint(1,3)
        print("Computer chose:\n")
        print(pool[comp_choice-1])
        if(choice != comp_choice):
            
            # Human wins
            if (choice == 1 and comp_choice == 3):
                print("You win")
            if (choice == 3 and comp_choice == 2):
                print("You win")
            if (choice == 2 and comp_choice == 1):
                print("You win")
            # Computer wins
            if (comp_choice == 1 and choice == 3):
                print("You lose")
            if (comp_choice == 3 and choice == 2):
                print("You lose")
            if (comp_choice == 2 and choice == 1):
                print("You lose")
        else:
            print("Game's a draw")
    else:
        print("You typed an invalid number, you lose")

    while True:
        answer = str(input('Run again? (y/n): ').lower())
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break