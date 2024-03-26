import random
from hangman_art import stages, logo
from words_database import words_list
from system import clear

print(logo)
print("\n\nWelcome to Hangman")

while True:
    word=words_list[random.randint(0,199)].lower()
    guessed_word=''
    print(word)

    for i in range(len(word)):
        guessed_word+='_'
    print(guessed_word)
    guess=list(guessed_word)

    flag=True
    hang_count=0
    while hang_count <= 6:
        g = input("Enter your guess ").lower()
        clear()
        if g in guess:
            print(f"You have already guessed {g}")
        for i in range(len(word)):
            if g == word[i]:
                guess[i]=g
                flag=False
        for i in range(len(guess)):
            print(guess[i],end="")
        print()
        if flag==True:
            hang_count+=1
            print("That's not in the word. You lose a life.")
            print(stages[hang_count])
        if hang_count == 6:
            print("Game over")
            break
        winner=True
        for i in range(len(guess)):
            if (guess[i]=='_'):
                winner=False
        if winner:
            print("You won")
            break
        flag=True
    while True:
        answer = str(input('Run again? (y/n): ').lower())
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        clear()
        continue
    else:
        print("Goodbye")
        break