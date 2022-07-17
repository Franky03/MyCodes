from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import lxml
import requests
from bs4 import BeautifulSoup

with open("./Udemy/DataEntry/data.txt") as file:
    link= file.readline()

chrome_driver_path= "C:\Development\chromedriver.exe"

class DataEntry:
    def __init__(self) -> None:
        self.headers= {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        self.response= requests.get(link, headers= self.headers)
        self.soup= BeautifulSoup(self.response.text, "lxml")
    
    def getLink(self):
        self.link_elements= self.soup.select(".list-card-link")
        self.all_links= []
        for link in self.link_elements:
            href= link.get('href')
            if 'http' not in str(href):
                self.all_links.append(f'https://www.zillow.com{href}')
            else:
                self.all_links.append(href)
        print(self.all_links)
        
    def getAddress(self):
        self.address_elements= self.soup.select('.list-card-addr')
        self.all_address= [address.text.split('|')[-1] for address in self.address_elements]
        print(self.all_address)
    
    def getPrice(self):
        self.price_elements= self.soup.select('.list-card-price')
        self.all_prices= [price.text.split('+')[0].replace('/mo', '') for price in self.price_elements if '$' in price.text]
        print(self.all_prices)
    
    def fillForms(self):
        self.driver= webdriver.Chrome(executable_path= chrome_driver_path)
        self.driver.maximize_window()
        self.driver.get('https://docs.google.com/forms/d/e/1FAIpQLSd9qZ_sUFeTrlBG87EoYymagvs-w7n1XtBAkhQ9hoDPB_IKSA/viewform?usp=sf_link')

        sleep(2)

        for n in range(len(self.all_prices)):

            self.adress_input= self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            self.price_input= self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            self.link_input= self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

            self.submit= self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')


            self.adress_input.send_keys(self.all_address[n])
            self.price_input.send_keys(self.all_prices[n])
            self.link_input.send_keys(self.all_links[n])

            self.submit.click()
            sleep(2)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
            sleep(2)
        


data= DataEntry()
data.getLink()
data.getAddress()
data.getPrice()
data.fillForms()