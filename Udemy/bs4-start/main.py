from bs4 import BeautifulSoup
from matplotlib.pyplot import cla
# import lxml

#Alguns sites podem não funcionar com html.parser, então importe o lxml e troque o parametro do soup.

with open("./Udemy/bs4-start/website.html", encoding="utf8") as file: #Tem que passar o encoding, caso contrário da erro de UnicodeDecode
    contents= file.read()

soup= BeautifulSoup(contents, 'html.parser')
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify()) #Printa todo código html só que com identação

#print(soup.p) #Pega o primeiro paragrafo ou o primeiro "a" ou qualquer outro

anchor= soup.find_all(name="a")
for tag in anchor:
    print(f"{tag.getText()}: {tag.get('href')}")

heading= soup.find(name="h1", id="name")
print(heading)

# section= soup.find(name='h3', class_="heading")
# print(section)

# company_url= soup.select_one(selector='.heading')
# print(company_url)

# Os dois acima dao o mesmo resultado

print(soup.select(".heading"))