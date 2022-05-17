from re import A
from threading import local


def mostraLinha(n):
    n=str(input('Digite a frase: '))
    print('-='* 20 )
    print(f'{n}')
    print('-='* 20 )

#mostraLinha()

def soma(a, b):
    print(f'{a} + {b} = ', end='')
    print(a+b)

soma(2, 7)

def contador(* num):
    print(f'Os valores são: {num} e ao todo são {len(num)} valores', end='')
    print()

contador(2,5,4)
contador(4,6,7,9)
contador(4,4,7,3,5,2,2,0)

lista=[2,5,4,6,7]
def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos] *= 2
        pos += 1
dobra(lista)
print(lista)

def somaa(*valores):
    s=0
    for num in valores:
        s += num
    print(f'A soma dos números {valores} é {s}')

somaa(2,6,4)
somaa(2,8)
somaa(4,7,8,8,4)

#Interactive help
#help(len) #Ajuda sobre alguma função

#Docstrings

def contador(i,f,p):
    """
    Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    """ 
    c=i
    while c<=f:
        print(c)
        c+=p

#help(contador)

#Parametros opcionais
def somar(a=0, b=0, c=0): #a, b e c estão sendo opcionais pq vc já declarou eles como 0
    s=a+b+c
    print(s)

somar(2,3,6)
somar(4,8)
somar()

#Escopo de variáveis

def teste():
    x=8 #Escopo/Variável Local
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')

n=2 #Escopo/Variável Global
print(f'No programa principal n vale {n}')
teste()
#print(f'No programa principal x vale {x}')  vai dar erro pq x foi declarado somente na funçao teste

def funcao():
    a=8 # a do escopo local
    print(f' "a" local vale {a}')

#a=5 # a do escopo global
#print(f' "a" global vale {a}')
funcao()

print('-='*20)
def tornar(b):
    global a #Usar o a global para esta função
    a=8
    b += 4
    c=2
    print(f' "a" local vale {a}')
    print(f' "b" local vale {b}')
    print(f' "c" local vale {c}')

a=12 #não vai contabilizr 12 com o global no escopo local
tornar(a)
print(f' "a" global vale {a}') #O a vai ser mudado pois na função o a global que é usado

def retornar(a=0,b=0,c=0):
    s=a+b+c
    return s

r1= retornar(2,6,4)
r2= retornar(6,4)
r3= retornar(8)
print(f'Os resultados foram : {r1}, {r2}, {r3}')

def fatorial(num=1):
    f=1
    for c in range(num, 0,-1):
        f *= c
    return f


n= int(input('Digite um número: '))
m= int(input('Digite um número: '))
print(f'O fatorial de {n} e {m} são: {fatorial(n)} e {fatorial(m)}')

def par(p=0):
    if p%2==0:
        return True
    else:
        return False

par(n)
if par(n)==True:
    print('É par!')
else:
    print('É impar!')