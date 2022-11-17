from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_driver_path= "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(ChromeDriverManager().install(), options= None)

driver.get("https://www.eloratings.net/")
driver.maximize_window()

time.sleep(3)

columns= driver.find_element(By.ID, 'itemdropdownColumns')
columns.click()

time.sleep(2)

cols= ['//*[@id="itemgrouphighest"]/span', '//*[@id="itemgrouplowest"]/span', 
'//*[@id="itemgroupchange3m"]/span', '//*[@id="itemgroupchange6m"]/span', '//*[@id="itemgroupchange2y"]/span', 
'//*[@id="itemgroupchange5y"]/span', '//*[@id="itemgroupchange10y"]/span']

for _id in cols:
    time.sleep(3)
    to_click= driver.find_element(By.XPATH, _id)
    time.sleep(3)
    to_click.click()

print('Done')