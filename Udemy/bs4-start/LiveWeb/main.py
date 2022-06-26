from bs4 import BeautifulSoup
import requests
import lxml

response= requests.get("https://news.ycombinator.com/newest")

# with open("./Udemy/bs4-start/LiveWeb/index.html", mode='w') as file:
#     file.write(response.text)
    
# with open("./Udemy/bs4-start/LiveWeb/index.html", mode='r') as file:
#     contents= file.read()

contents= response.text

soup= BeautifulSoup(contents, "lxml")
anchor= soup.find_all(name="a", class_='titlelink')
upvote= soup.find_all(name="span", class_='score')
# for c in range(0, len(anchor)):
#     print("-="*20)
#     print(f"{anchor[c].getText()}\n {anchor[c].get('href')} ")
#     print(upvote[c].getText().split()[0])

title_list=[title.getText() for title in anchor]
links= [link.get('href') for link in anchor]
scores= [int(up.getText().split()[0]) for up in upvote]

max_score= max(scores) 
index= scores.index(max_score)
print(f"{title_list[index]}\n{links[index]}\n{max_score}")