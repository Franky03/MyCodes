from selenium import webdriver

chrome_driver_path= "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.youtube.com") #Open a window

# driver.close() #fecha apenas uma aba
driver.quit() #fecha o navegador inteiro