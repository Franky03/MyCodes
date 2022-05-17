from time import sleep
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shif):
    letters=[]
    new= []
    for l in text:
        if l != ' ':
            letters.append(l)
    for i in range(0, len(letters)):
        pos= alphabet.index(letters[i])
        pos += shif
        new.append(alphabet[pos])
    print("--"*20)
    print(f"The text is: {text}")
    print('The encoded text is: ', end='')
    for c in new:
        print(f"{c}", end='')
    print()
    print("--"*20)

def decrypt(text, shif):
    letters=[]
    new=[]
    for l in text:
        if l !=' ':
            letters.append(l)
    for i in range(0, len(letters)):
        pos= alphabet.index(letters[i])
        pos -= shif
        new.append(alphabet[pos])
    print("--"*20)
    print(f"The text is: {text}")
    print('The encoded text is: ', end='')
    for c in new:
        print(f"{c}", end='')
    print()
    print("--"*20)

def cesar(text, shif, option):
    new=''
    for i in text:
        if i in alphabet:
            pos= alphabet.index(i)
            if option==0:
                pos += shif
            elif option==1:
                pos -= shif
            new= new + alphabet[pos]
        else:
            new += i
    print("--"*20)
    print(f"The text is: {text}")
    print(f'The encoded text is: {new}')
    print()
    print("--"*20)



#Programa principal
while True:
    print(f"{'Ceasar Cipher':^40}")
    print('--'*20)
    print(f"{'[0] ENCODE':<10}\n{'[1] DECODE':<10}\n{'[2] EXIT':<10}")
    print('--'*20)
    while True:
        direction= int(input("Type encode to encrypt, type decode to decrypt: "))
        if direction<=2:
            break
        else:
            print("ERROR")
    if direction<=1:
        texto= str(input("Type the message: ")).lower()
        shift= int(input("Type the shift number: "))
        shift= shift % 26
        cesar(texto, shift, direction)
        sleep(2)
    else:
        break