##################### Extra Hard Starting Project ######################

import pandas as pd
import datetime as dt
import smtplib
import random

# 1. Update the birthdays.csv
data= pd.read_csv('./Udemy/Day32FP/birthdays.csv')
print(data)

# 2. Check if today matches a birthday in the birthdays.csv
date= dt.datetime.now()
month= date.month
day= date.day
today= (month, day)
birthday_dict= {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}


def check_day():
    if today in birthday_dict:
        return True
    return False

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if check_day:
    let= random.randint(1,3)
    with open(f'./Udemy/Day32FP/letter_templates/letter_{let}.txt') as letter:
        sent_letter= letter.read()
        sent_letter= sent_letter.replace('[NAME]', birthday_dict[today]['name'])
    
    print(sent_letter)
    
    
    # string= ''
    # for c in sent_letter:
    #     if c =='Dear [NAME],\n' or c=='Hey [NAME],\n':
    #         c= c.replace('[NAME]', birthday_dict[today]['name'])
    #     string+=c
    # print(string)
    

# 4. Send the letter generated in step 3 to that person's email address.

my_email= 'pythonaula04@gmail.com'
password='cemdiascode'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user= my_email, password=password)
    connection.sendmail(from_addr= my_email, to_addrs=birthday_dict[today]['email'], msg=f'Subject:Happy Birthday\n\n{sent_letter}')

print('OK')