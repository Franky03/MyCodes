aluno= dict()
aluno['Nome']= str(input('Nome do aluno: '))
aluno['Média']= float(input('Média do aluno: '))
if aluno['Média']>=7:
    aluno['Situação']= 'Aprovado'
elif aluno['Média']>5 and aluno['Média']<7:
    aluno['Situação']= 'Recuperação'
else:
    aluno['Situação']= 'Reprovado'
print('=-'*20)
for k, v in aluno.items():
    #print(f"- Aluno: {aluno['Nome']}\n- Média: {aluno['Média']}\n- Situação: {aluno['Situação']}")
    print(f'- {k}: {v}')
print('=-'*20)
