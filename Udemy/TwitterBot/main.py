from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISSED_DOWN, PROMISSED_UP = 80, 80
TWITTER_USER= 'YOUR USER OR EMAIL OR NUMBER'
TWITTER_PASSWORD= 'YOUR PASSWORD'
chrome_driver_path= "C:\Development\chromedriver.exe"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver= webdriver.Chrome(executable_path= chrome_driver_path)
        self.up= 0
        self.down=0
        self.driver.maximize_window()
    
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        
        sleep(15)

        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        sleep(60)

        self.down= float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)

        self.up= float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

        print(f'Down: {self.down}\nUp:{self.up}')

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/')
        
        sleep(5)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div').click()

        except:
            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[2]/div[4]/div[2]/span/span').click()
            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[2]/a/div').click()
        
        try:
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[2]/div/div/div/div/div[2]/div/div[1]/a').click()
        except:
            pass

        sleep(3)

        self.email= self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.email.send_keys(TWITTER_USER)
        self.email.send_keys(Keys.ENTER)

        sleep(3)

        self.key= self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.key.send_keys(TWITTER_PASSWORD)
        self.key.send_keys(Keys.ENTER)
        
        sleep(6)

        self.write= self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        self.write.click()
        
        sleep(2)

        tweet= f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISSED_DOWN}down/{PROMISSED_UP}up?"

        self.box= self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        sleep(2)
        self.box.send_keys(tweet)
        sleep(1)
        self.go= self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div')

        self.go.click()

        sleep(3)

        self.driver.quit()

bot= InternetSpeedTwitterBot()

bot.get_internet_speed()
sleep(1)
bot.tweet_at_provider()
