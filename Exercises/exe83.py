expr= str(input('Digite uma expressão: '))
pilha=[]
for s in pilha:
    if s=='(':
        pilha.append('(')
    elif s==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('A expressão está correta')
else:
    print('A expressão está errada')