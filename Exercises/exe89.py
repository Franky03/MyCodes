boletim= []
while True:
    nome= str(input('Nome: '))
    notaum= float(input('Nota 1: '))
    notadois= float(input('Nota 2: '))
    media= (notaum + notadois)/2
    boletim.append([nome, [notaum, notadois], media])
    escolha= str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha in 'nN':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for i,a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('=-'*30)
while True:
    print('=-'*30)
    aluno= int(input('Quer ver a nota de qual aluno? [999 para parar]: '))
    if aluno==999:
        print("FIM")
        break
    if aluno <= len(boletim)-1:
        print(f'As notas de {boletim[aluno][0]} são: {boletim[aluno][1]}')
    else:
        print('Número inválido')