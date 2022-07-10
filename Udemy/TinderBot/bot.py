from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


print('TESTE')

options= webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_driver_path= "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path= chrome_driver_path, options= options)
driver.maximize_window()

driver.get('https://tinder.com/')
sleep(2)
driver.find_element(By.XPATH, '//*[@id="q-996647900"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()
sleep(2)

driver.switch_to(driver.window_handles[1])

sleep(1)
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('pythonaula04@gmail.com')
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys('cemdiascode')
driver.find_element(By.XPATH, '//*[@id="u_0_0_dj"]').click()
