from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options= webdriver.ChromeOptions()
options.add_argument("--headless")

chrome_driver_path= "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path= chrome_driver_path, options= None)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie= driver.find_element(By.ID, "cookie")

store= driver.find_elements(By.CSS_SELECTOR, "#store div")
items_id= [items.get_attribute("id") for items in store]

timeout= time.time() + 5 #5 segundos
five= time.time() + 60*5 #5 minutos


while True:
    cookie.click() 

    if time.time()> timeout: #Se o tempo desde ser iniciado for maior que 5 segundos...
        all_prices= driver.find_elements(By.CSS_SELECTOR, '#store b') #Pega todos as tags de preço da store
        item_prices=[]

        for price in all_prices:
            price_text= price.text
            if price_text != '':
                custo=int(price_text.split('-')[1].strip().replace(",", "")) #Pegar os textos dessa tag e selecionar o custo
                item_prices.append(custo)
        
        cookie_update= {}
        for n in range(len(item_prices)):
            cookie_update[item_prices[n]]= items_id[n] #Cria um dicionário com os custos e seus respectivos ids

        money= driver.find_element(By.ID, "money").text #Pega o total de cookies que já tem no site (o dinheiro)
        if  "," in money:
            money= money.replace(",", "")
        cookie_count= int(money)

        aff_upgrades= {} 
        for cost, id in cookie_update.items():
            if cookie_count> cost: #Se o total de cookies for maior que o custo do loop
                aff_upgrades[cost]= id # esses custos e ids irão para um novo dicionário
        
        higest_price= max(aff_upgrades) #pega o maior preço do dicionário anterior
        print(higest_price)
        to_purch_id= aff_upgrades[higest_price] #E pega o id pelo maior preço
        

        driver.find_element(By.ID, to_purch_id).click() #Clica no item de maior preço
        
        timeout= time.time() + 5 #Adiciona mais cinco segundos

    if time.time()> five: #Se o tempo de execução for maior que 5 minutos, ele para
        cookie_per_sec= driver.find_element(By.ID, "cps").text
        print(cookie_per_sec)
        break