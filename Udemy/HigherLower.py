import random
from resources import data

#choice anyone

def compare():
    already=[]
    win=False
    score=0
    while True:
        while True: #Garantir que não sorteie duas opções iguais
            if not win:
                n= random.randint(0, len(data)-1)
                person1= data[n]
            elif win:
                person1= person2
            while True:
                m= random.randint(0, len(data)-1)
                person2= data[m]
                if m not in already:
                    already.append(m)
                    break
            if n!=m:
                break
        print('__'*40)
        print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.\nVS")
        print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}.")
        print('__'*40)
        a= person1['follower_count']
        b= person2['follower_count']
        if a>=b:
            champ= person1
        elif a<b:
            champ=person2
        while True:
            choice= str(input("Who has more followers? Type 'A' or 'B': ")).upper().strip()
            if choice=='A' or choice=='B':
                break
            else:
                print("ERROR")
        if choice=='A':
            choice= person1
        else:
            choice= person2
        if choice== champ:
            score += 1
            print(f"You're right! Current Score: {score}")
            win= True
        else:
            print(f"Sorry, that's wrong. Final Score: {score}")
            break

#Play the game again

def game():
    while True:
        compare()
        while True:
            resp= str(input("Wanna play again ? [Y/N]: ")).upper().strip()[0]
            if resp=='Y' or resp=='N':
                break
            else:
                print("ERROR")
        if resp=='N':
            print("Bye Bye!")
            break

game()