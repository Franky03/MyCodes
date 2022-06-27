from bs4 import BeautifulSoup
import requests

response= requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents= response.text
soup= BeautifulSoup(contents, 'html.parser')

titles= soup.find_all(name="h3", class_="title")

with open("./Udemy/100Movies/movies.txt", mode="w") as file:
    for c in range(len(titles)-1, -1, -1):
        if c==0:
            file.write(f"{titles[c].getText()}")
        else:  
            file.write(f"{titles[c].getText()}\n")
