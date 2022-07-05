import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import re

url= "https://www.magazineluiza.com.br/hd-externo-1tb-adata-ahv620s-1tu31-cbk-usb-3-1/p/227247900/in/hdex/"

header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

response= requests.get(url, headers=header)

soup= BeautifulSoup(response.content, "lxml") #Usar o .content ou .text para obter o html, caso contrário dá erro
price= float(soup.find("p", class_="sc-hKwDye dWfgMa sc-cfJLRR wDYkg").get_text().split("R$")[1].replace(',','.').strip())
print(price)

if price<=260.0:
    title= soup.find("h1", class_="sc-hKwDye ihAhDB").get_text().strip()
    print(title)

    my_email= "aulapython@yahoo.com"
    my_password= "rgjbetpmvlhhqznv"

    mensagem= f"Subject:Amazon Price Arlet!!\n\n{title}\nR${price}\n{url}"
    mensagem= mensagem.encode("utf-8")


    with smtplib.SMTP('smtp.mail.yahoo.com', port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(my_email, "pythonaula04@gmail.com", msg= mensagem)