from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options= webdriver.ChromeOptions()
options.add_argument("--headless")

chrome_driver_path= "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path= chrome_driver_path, options= None)

driver.get("https://www.linkedin.com/")

#Login

enter= driver.find_element(By.XPATH, '/html/body/nav/div/a[2]').click()

email= driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('pythonaula04@gmail.com')
password= driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('cemdiascode')
finish= driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

try:
    driver.find_element(By.XPATH, '//*[@id="ember455"]/button').click()
except:
    pass

