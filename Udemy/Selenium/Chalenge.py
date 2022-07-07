from selenium import webdriver
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_argument("--headless")

chrome_driver_path= "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path= chrome_driver_path, options=options)

driver.get("https://www.python.org")
menu= driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li")


events={}
for c in range(0, len(menu)):
    date= menu[c].find_element(By.TAG_NAME, "time").get_attribute("datetime")[:10]
    ev= menu[c].find_element(By.TAG_NAME, "a").text
    events[c]= {"time": date, "name": ev}

print(events)


driver.quit()