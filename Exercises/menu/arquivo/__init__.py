from menu.interface import *

def arquivoExiste(nome):
    try:
        a= open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a= open(nome, 'wt+')
        a.close()
    except:
        print('ERRO! Arquivo não foi criado.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

def lerArquivo(nome):
    try:
        a= open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado= linha.split(';')
            dado[1]= dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(nome, n='desconhecido', i=0):
    try:
        a= open(nome, 'at')
    except:
        print('Erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{n};{i}\n')
        except:
            print('Erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {n} adicionado!')
            a.close()