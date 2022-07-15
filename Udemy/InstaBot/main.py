from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SIMILAR= 'luizalabs'
USERNAME= 'pythonaula04'
PASSWORD= '************'

options= webdriver.ChromeOptions()

chrome_driver_path= "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path= chrome_driver_path, options= options)

driver.get('https://www.instagram.com/')
