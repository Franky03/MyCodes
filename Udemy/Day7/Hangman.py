import random
from words import words
from hang_visual import lives_visual_dict


while True:
    life=6
    word= random.choice(words).upper()
    while '-' in word or ' ' in word:
        word= random.choice(words).upper()
    letters= []
    for l in word:
        letters.append(l)
    #print(word)
    display= []
    word_length= len(letters)
    for i in range(0, word_length):
        display.append('_')
    print(display)
    already= []
    while display != letters:
        if life==0:
            break
        guess= str(input("Guess a letter: ")).upper()
        if guess in already:
            if guess in display:
                print(f"You already guessed {guess}.")
            else:
                print(f"You already typed, {guess} is not in the word.")
        else:
            for position in range(word_length):
                letter= word[position]
                if letter == guess:
                    display[position] =letter 
            if guess not in letters:
                life -= 1
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                print(lives_visual_dict[life])
                if life==0:
                    break
            else:
                print(lives_visual_dict[life])
            print(f"Lifes: {life}")
            print(display)
            already.append(guess)
    if life>0:
        print("YOU WON")
    else:
        print(f"The word was: {word}!\n")
        print("YOU LOSE")
    while True:
        quest= str(input("Want to play again ? [Y/N]: ")).upper().strip()[0]
        if quest in 'YyNn':
            break
        else:
            print("Type a valid answer!")
    if quest in 'Nn':
        print("END")
        break