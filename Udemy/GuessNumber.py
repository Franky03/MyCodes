import random

#Function to check user's guess against actual answer.
def result(player, num, turn):
    if player>num:
        print(f"Too High!")
        return turn-1
    if player<num:
        print(f"Too Low!")
        return turn-1
    if player==num:
        print(f"You got it! The answer was {num}")

#Make function to set difficulty.
def mode():
    while True:
        option= int(input(f"{'Dificulty':^20}\n[0]Easy\n[1]Hard\nChoose: "))
        if option==1 or option==0: 
            break
        else:
            print("ERROR")
    if option==0:
        return easy
    else:
        return hard

hard=5
easy=10

def game():
    print("Welcome to the Number Guessing Game!")
    #Choosing a random number between 1 and 100
    num= random.randint(1, 100)
    print("I'm thinking in a number between 1 and 100.")
    #print(num)
    print('__'*10)
    turns= mode()
    #Repeat the guessing functionality if they get it wrong
    guess=0
    while guess!=num:
        print("__"*30)
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the Player Guess a Number
        guess= int(input('Guess a number: '))
        #Track the number of turns and reduce by 1 if they get it wrong.
        turns= result(guess, num, turns)
        if turns==0:
            print(f"You've run out of guesses, you lose. The answer was {num}.")
            return
        elif guess!=num:
            print("Guess again.")

while True:
    game()
    while True:
        resp= str(input("Play again ? [Y/N]: ")).upper().strip()[0]
        if resp=='Y' or resp=='N':
            break
        else:
            print("ERROR")
    if resp=='N':
        break