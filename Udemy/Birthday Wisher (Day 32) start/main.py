import smtplib
import datetime as dt
import random

my_email= 'pythonaula04@gmail.com'
password='cemdiascode'
ya_email= 'aulapython@yahoo.com'
ya_password='wrvbvrpbtqerbxqy'


now= dt.datetime.now()
day_of_week= now.weekday()
if day_of_week==3:
    with open('./Udemy/Birthday Wisher (Day 32) start/quotes.txt') as file:
        quotes= file.readlines()
        the_quote= random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email, password=password)
        connection.sendmail(from_addr=my_email, 
        to_addrs='aulapython@yahoo.com', 
        msg=f"Subject:Be Happy\n\n{the_quote}")



# #Gmail
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user= my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#     to_addrs='aulapython@yahoo.com', 
#     msg="Subject:Gmail Code\n\nThis is the body of my email(Gmail)")

# #Yahoo
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user= ya_email, password=ya_password)
#     connection.sendmail(from_addr=ya_email, 
#     to_addrs= my_email, 
#     msg="Subject:Yahoo Code\n\nThis is the body of my email(Yahoo)")



# now= dt.datetime.now()
# year= now.year
# month= now
# day_of_week= now.weekday()
# print(day_of_week, month, year)

# date_of_birth= dt.datetime(year=2004, month=10, day=1)
# print(date_of_birth)
