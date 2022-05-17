import random
from time import sleep

#Functions

def card(turn):
    card= random.choice(baralho)
    turn.append(card)
    baralho.remove(card)

def total(turn):
    total=0
    face=['Q', 'K', 'J']
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total>11:
                total +=1
            else:
                total +=11 
    if total==21 and len(turn)==2:
        return 0
    return total

def compare(score_p, score_d):
    global wins
    global loses
    global draws
    if score_p==score_d:
        draws+=1
        return 'Draw!'
    elif score_p==0:
        wins+=1
        return "You Win with a BlackJack!"
    elif score_d==0:
        loses+=1
        return 'You Lose, dealer has a BlackJack!'
    elif score_p>21:
        loses+=1
        return 'You went over ,You Lose!'
    elif score_d>21:
        wins+=1
        return 'Dealer went over, You Win!'
    elif score_p> score_d:
        wins+=1
        return "You Win!"
    else:
        loses+=1
        return "You Lose!"

def emb(text):
    print(text, end='')
    for c in range(0,4):
        sleep(0.5)
        print('.', end='', flush=True)
        sleep(0.5)
    print()

#Principal Program
wins=0
loses=0
draws=0
while True:
    baralho=[2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A',]
    dealer= []
    player=[]
    game_over=False
    for _ in range(2):
        card(player)
        card(dealer)
    while True:
        score_p= total(player)
        score_d= total(dealer)
        print("--"*20)
        print(f" Your cards: {player}, current score: {score_p}")
        print(f" Dealer's firt card: {dealer[0]}")
        print("--"*20)
        if score_p==0 or score_d==0 or score_p>21:
            game_over=True
        else:
            while True:
                user_choice= str(input("[Y]Get Another Card\n[N]Pass\nChoice: ")).upper().strip()
                if user_choice=='Y' or user_choice=='N':
                    break
                else:
                    print('ERROR')
            print("--"*20)
            if user_choice=='Y':
                emb('Shuffling')
                card(player)
            else:
                game_over= True
        if game_over:
            break
    while score_d !=0 and score_d < 17:
        card(dealer)
        score_d= total(dealer)
    print(f"You have: {player} For a total of: {score_p}\nDealer have: {dealer} For a total of: {score_d}!")
    print(compare(score_p, score_d))
    resp=''
    while True:
        resp= str(input("Want to play again? [Y/N]: ")).upper().strip()[0]
        if resp=='Y' or resp=='N':
            break
        else:
            print("ERROR")
    if resp=='N':
        print('--'*10)
        print(f"Total wins: {wins}\nTotal loses: {loses}\nTotal draws: {draws}\nEND")
        break
    else:
        player.clear()
        dealer.clear()
