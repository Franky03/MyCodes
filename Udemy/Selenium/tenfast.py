from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options= webdriver.ChromeOptions()
options.add_argument("--headless")

chrome_driver_path= "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path= chrome_driver_path, options= None)


driver.get("https://10fastfingers.com/typing-test/portuguese")

try:
    button= driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyButtonDecline"]')
    button.click()
except:
    pass

sleep(2)
words= driver.find_elements(By.CSS_SELECTOR, "#words #row1 span")
bar= driver.find_element(By.XPATH, '//*[@id="inputfield"]')
veri=0

while True:
    for c in range(22):
        word= driver.find_element(By.CLASS_NAME, "highlight")    
        bar.send_keys(word.text)
        bar.send_keys(Keys.SPACE)
        veri+=1
    if veri%22==0:
        words= driver.find_elements(By.CSS_SELECTOR, "#words #row1 span")
    if veri== len(words):
        break

