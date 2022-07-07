from selenium import webdriver
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_argument("--headless")

chrome_driver_path= "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path= chrome_driver_path, options= None)


driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles= driver.find_element(By.CSS_SELECTOR, '#articlecount a')

print(int((articles.text).replace(',','')))
print(articles.tag_name)

bar= driver.find_element(By.XPATH, '//*[@id="searchInput"]')
bar.click()
bar.send_keys("Superman")
bar.submit()

driver.quit()
