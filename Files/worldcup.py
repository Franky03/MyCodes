from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv

class MakeTable():

    def __init__(self, url):
        self.site= url
        self.cells= False
        self.string1= []
        self.soup= None
        self.colls= None

    def get_content(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        driver= webdriver.Chrome(ChromeDriverManager().install(), options= None)
        driver.get(self.site)
        sleep(1)
        driver.maximize_window()
        sleep(5)
        response= driver.page_source
        self.soup= BeautifulSoup(response, 'html.parser')

        driver.quit()

        self.cells= self.soup.find_all('div', {'class': 'slick-cell'})
    

    def to_csv(self):
        try:
            with open('./table.csv', 'w', encoding="utf-8", newline='') as file:
                row=[]
                for c in range(len(self.cells)):
                    word= self.cells[c].getText()
                    if c % 16 != 0:
                        row.append(word)
                    if c<=16:
                        if (c!=0 and c % 15 == 0):
                            self.string1.append(row)
                            row=[]
                    else:
                        if (c % 16 == 0):
                            self.string1.append(row)
                            row=[]
                

                writer= csv.writer(file)
                writer.writerows(self.string1)
                print(self.string1)
        except Exception as e:
            print(e)
    
    def run(self):
        self.get_content()
        self.to_csv()

        return True
    
    def get_goals(self):
        self.soup.find_all('div', {'class': ''})

mt= MakeTable("https://www.eloratings.net/")
mt.run()