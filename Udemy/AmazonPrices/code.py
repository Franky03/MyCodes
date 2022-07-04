import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url= "https://www.amazon.com.br/Externo-Port%C3%A1til-UnionSine-compat%C3%ADvel-Notebook/dp/B09XM97K91/ref=sr_1_1_sspa?keywords=hd%2Bexterno&qid=1656880627&sprefix=hd%2Bext%2Caps%2C393&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.4bb5663b-6f7d-4772-84fa-7c7f565ec65b&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyT0k4MEczT05HNTNOJmVuY3J5cHRlZElkPUEwMzI2ODE0MTFMQVJQWk5JSERGTiZlbmNyeXB0ZWRBZElkPUEwNjM2NzI5U1Q3RzZLU1NFMzJZJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"

header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

response= requests.get(url, headers=header)

soup= BeautifulSoup(response.text, 'lxml') #Usar o .content ou .text para obter o html, caso contrário dá erro
price= float(soup.find("span", class_="a-offscreen").get_text().split("R$")[1].replace(',','.'))
print(price)

if price<=250.0:
  title= soup.find("span", id= "productTitle").get_text().strip()
  print(title)

  my_email= "aulapython@yahoo.com"
  my_password= "rgjbetpmvlhhqznv"

  mensagem= f"Subject:Amazon Price Arlet!!\n\n{title}\nR${price}\n{url}"
  mensagem= mensagem.encode("utf-8")


  with smtplib.SMTP('smtp.mail.yahoo.com', port=587) as connection:
      connection.starttls()
      connection.login(my_email, my_password)
      connection.sendmail(my_email, "pythonaula04@gmail.com", msg= mensagem)