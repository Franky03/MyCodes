from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

facebook= driver.window_handles[1]
print(driver.title)
driver.switch_to.window(facebook)

sleep(2)
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('pythonaula04@gmail.com')
sleep(1)
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys('cemdiascode')
sleep(1)
driver.find_element(By.XPATH, '//*[@id="loginbutton"]').click()
sleep(1)


base_window = driver.window_handles[0]
driver.switch_to.window(base_window)
print(driver.title)

sleep(8)
permitir= driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div/div/div[3]/button[1]/span')
permitir.click()
sleep(1)
n_interesse= driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div/div/div[3]/button[2]')
n_interesse.click()
sleep(1)
aceitar= driver.find_element(By.XPATH, '//*[@id="q-996647900"]/div/div[2]/div/div/div[1]/div[1]/button')
aceitar.click()

sleep(5)
for n in range(80):
    sleep(2)
    try:
        fechar_match= driver.find_element(By.XPATH, '//*[@id="q-666276699"]/div/div/div[1]/div/div[4]/button')
        fechar_match.click()
        sleep(1)
    
    except:
        pass

    try:
        nao_interesse= driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div[2]/button[2]')
        nao_interesse.click()
        sleep(1)

    except:
        pass

    try:
        print('called')
        X= driver.find_element(By.XPATH, '//*[@id="q-996647900"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        X.click()

    except:
        print('called2')
        X= driver.find_element(By.XPATH, '//*[@id="q-996647900"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        X.click()

    
        