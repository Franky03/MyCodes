##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import smtplib

# 1. Update the birthdays.csv
data= pd.read_csv('./Udemy/Day32FP/birthdays.csv')
print(data)

# 2. Check if today matches a birthday in the birthdays.csv
date= dt.now()
month= date.month
day= date.day
today= (day, month)
bithday= (5,26)

def check_day():
    if today== bithday:
        return True
    return False

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




