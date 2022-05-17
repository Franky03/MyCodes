from menu.interface import *
from menu.arquivo import *
from time import sleep

arq= 'Pessoas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta= menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resposta==1:
        #Opção de ler arquivos de pessoas cadastradas
        lerArquivo(arq)
    elif resposta==2:
        #Opção para cadastrar uma nova pessoa
        cabeçalho('CADASTRAR NOVA PESSOA')
        nome= str(input('Nome da pessoa: '))
        idade= leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta==3:
        cabeçalho('Saindo do sistema! Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida.')
    sleep(1)