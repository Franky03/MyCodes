from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
# bar.send_keys(Keys.ENTER) press enter
bar.submit()

driver.find_element(By.LINK_TEXT, "DC Comics").click()

# driver.quit()
