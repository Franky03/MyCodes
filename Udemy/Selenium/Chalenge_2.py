from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options= webdriver.ChromeOptions()
options.add_argument("--headless")

chrome_driver_path= "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path= chrome_driver_path, options= None)


driver.get("http://secure-retreat-92358.herokuapp.com")


bar= driver.find_elements(By.CLASS_NAME, "form-control")

content= ["Franky", "Super", "emaildaora@gmail.com"]

for t in range(len(bar)):
    bar[t].send_keys(content[t])
    

button= driver.find_element(By.XPATH, "/html/body/form/button")
button.click()

# driver.quit()