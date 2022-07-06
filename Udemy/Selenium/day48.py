from selenium import webdriver
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_argument("--headless")

#Para deixar o chrome rodando em segundo plano é preciso passar o parametro options no driver e rodar as duas linhas acima

chrome_driver_path= "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path=chrome_driver_path, chrome_options= options)


driver.get("https://www.python.org/") #Open a window
title= driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
link= driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

""""
find elements by...

find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")

"""
# driver.get("https://www.amazon.com.br/Externo-Port%C3%A1til-UnionSine-compat%C3%ADvel-Notebook/dp/B09XM97K91/ref=sr_1_1_sspa?keywords=hd%2Bexterno&qid=1656880627&sprefix=hd%2Bext%2Caps%2C393&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.4bb5663b-6f7d-4772-84fa-7c7f565ec65b&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyT0k4MEczT05HNTNOJmVuY3J5cHRlZElkPUEwMzI2ODE0MTFMQVJQWk5JSERGTiZlbmNyeXB0ZWRBZElkPUEwNjM2NzI5U1Q3RzZLU1NFMzJZJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1")

# price= driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]')
# print(price)


print(title)
print(title.text)
print(title.tag_name)
print(title.get_attribute("placeholder"))
print(link.get_attribute("href"))

# driver.close() #fecha apenas uma aba
driver.quit() #fecha o navegador inteiro