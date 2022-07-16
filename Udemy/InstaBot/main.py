from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

SIMILAR= 'luizalabs'
USERNAME= '1snt4_b0t'
PASSWORD= '***'

chrome_driver_path= "C:\Development\chromedriver.exe"


class InstaFollower:
    def __init__(self):
        self.options= webdriver.ChromeOptions()
        self.driver= webdriver.Chrome(executable_path= chrome_driver_path, options= self.options)
        self.driver.maximize_window()

    def login(self):

        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(3)
        self.email= self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.email.send_keys(USERNAME)
        sleep(1)
        self.password= self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password.send_keys(PASSWORD)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(5)

    def find_followers(self):
        self.driver.get(f'https://www.instagram.com/{SIMILAR}')
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a').click()
# 
    def follow(self):
        
        while True:

            try:
                list_people= self.driver.find_elements(By.CSS_SELECTOR, 'li button')
                for person in list_people:
                    if person.text=='Seguir':
                        person.click()
                        sleep(3)
                print(len(list_people))

                self.driver.execute_script("argument[0].scrollIntoView(true);", list_people[-1])
            except ElementClickInterceptedException:
                cancel= self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/button[2]')
                cancel.click()

bot= InstaFollower()
bot.login()
bot.find_followers()
bot.follow()