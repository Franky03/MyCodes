import random 
playerIn= True
dealerIn=True
deck=[2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A',]
playerHand= []
dealerHand=[]

def dealCard(turn):
    card= random.choice(deck)
    turn.append(card)
    deck.remove(card)

def total(turn):
    total=0
    face=['J','K','Q']
    for card in turn:
        if card in range(1,11):
            total+=card
        elif card in face:
            total +=10
        else:
            if total>11:
                total+=1
            else:
                total+=11
    return total

def revealDealerHand():
    if len(dealerHand)==2:
        return dealerHand[0]
    elif len(dealerHand)>2:
        return dealerHand[0],[1]

for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerIn or dealerIn:
    print(f"Dealer had {revealDealerHand()} and X")
    print(f"You have {playerHand} for a total of {total(playerHand)}.")
    if playerIn:
        stayOrHit= input("1: Stay\n2: Hit\n")
    if total(dealerHand)>16:
        dealerIn=False
    else:
        dealCard(dealerHand)
    if stayOrHit=='1':
        playerIn==False
    else:
        dealCard(playerHand)
    if total(playerHand)>=21:
        break
    elif total(dealerHand)>=21:
        break

if total(playerHand)==21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and {dealerHand} for a total of {total(dealerHand)}")
    print("BlackJack! You Win!")
elif total(dealerHand)==21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and {dealerHand} for a total of {total(dealerHand)}")
    print("BlackJack! Dealer wins")
elif total(playerHand)>21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and {dealerHand} for a total of {total(dealerHand)}")
    print("You bust! Dealer Wins!")
elif total(dealerHand)>21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer bust! You win!")
elif 21- total(dealerHand)< 21- total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer Wins !")
elif 21-total(dealerHand)> 21- total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and {dealerHand} for a total of {total(dealerHand)}")
    print("You Win !")
