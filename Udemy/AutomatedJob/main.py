from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


print('TESTE')

options= webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_driver_path= "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(executable_path= chrome_driver_path, options= options)
driver.maximize_window()

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

#Login
sleep(3)
driver.find_element(By.XPATH, '/html/body/div[3]/a[1]').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('pythonaula04@gmail.com')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('cemdiascode')
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
sleep(20)
jobs= driver.find_elements(By.CSS_SELECTOR,'.jobs-search-results__list li')
print(f"Applying for {len(jobs)} jobs...")
for job in jobs:
    job.click()
    sleep(2)
    try:
        btn= driver.find_element(By.CSS_SELECTOR,'.jobs-apply-button--top-card button')
        btn.click()
        sleep(2)

        phone= driver.find_element(By.CSS_SELECTOR, '.fb-single-line-text .display-flex input')
        if phone.text== "":
            phone.send_keys('667562499')
        
        s_btn= driver.find_element(By.CSS_SELECTOR, 'footer button')
        if s_btn.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            s_btn.click()

        sleep(2)

        s_btn.click()
        
        try:
            field= driver.find_elements(By.CSS_SELECTOR, '.fb-single-line-text .display-flex input')
            
            for f in field:
                if f.text=="":
                    f.send_keys('2')
                else:
                    pass
            sleep(1)
        except:
            continue

        try:
            yes= driver.find_elements(By.CSS_SELECTOR, '.fb-radio-buttons .fb-radio label')
            yes[0].click()
            sleep(1)
        except:
            pass
        
        contin= driver.find_elements(By.CSS_SELECTOR, 'footer .display-flex button')
        contin[1].click()

        try:
            driver.find_elements(By.CSS_SELECTOR, '.fb-radio-buttons .display-flex label')[0].click()
            this_pg= driver.find_elements(By.CSS_SELECTOR, 'footer .display-flex button')
            this_pg[1].click()
        except:
            pass
        
        sleep(2)
        
        finish= driver.find_elements(By.CSS_SELECTOR, 'footer .display-flex button')
        print(finish)
        finish[1].click()
        
        close= driver.find_element(By.CLASS_NAME, '.artdeco-modal button')
        close.click()
        
    except:
        print("No application button, skipped.")
        continue
    


