import urllib
import urllib.request

try:
    site= urllib.request.urlopen('http://www.pudim.com.br') #Verificar se o site está ou não dispo
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui entrar no site Pudim!')
    #print(site.read())