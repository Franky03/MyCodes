frase= str(input('Digite seu nome')).strip()
print('Seu nome em maiusculo é {}'.format(frase.upper()))
print('Seu nome em minusculo é {}'.format(frase.lower()))
print('Seu nome tem ao todo {} letras'.format(len(frase) - frase.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(frase.find(' ')))
separa= frase.split()
num= int(input('Digite um número: '))
u= num// 1 % 10
d = num// 10 % 10
c= num// 100 % 10
m = num// 1000 % 10
print ('Analisando o número {}'.format(num))
print ('Unidade: {}'.format(u))
print ('Dezena: {}'.format(d))
print ('Centena: {}'.format(c))
print ('Milhar: {}'.format(m))
cid= str(input('Em que cidade voce nasceu?')).strip()
print(cid[:5]== 'Santo')
nome = str(input('Digite seu nome: ')).strip()
print('Seu nome tem Silva ?{}'.format('Silva' in nome.title()))
nomi= str(input ('Qual o seu nome?')).strip().lower()
print('O seu nome tem {} letras'.format(len(nomi)))
print('O seu nome tem {} letras A'.format(nomi.count('a')))
print('A primeira letra A apareceu na posiçao {}'.format(nomi.find('A')))