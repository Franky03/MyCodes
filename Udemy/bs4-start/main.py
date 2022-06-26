from bs4 import BeautifulSoup
# import lxml

#Alguns sites podem não funcionar com html.parser, então importe o lxml e troque o parametro do soup.

with open("./Udemy/bs4-start/website.html", encoding="utf8") as file: #Tem que passar o encoding, caso contrário da erro de UnicodeDecode
    contents= file.read()

soup= BeautifulSoup(contents, 'html.parser')
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify()) #Printa todo código html só que com identação

#print(soup.p) #Pega o primeiro paragrafo ou o primeiro "a" ou qualquer outro

print(soup.find_all(name="a"))
