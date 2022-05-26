import smtplib

my_email= 'pythonaula04@gmail.com'
password='cemdiascode'
ya_email= 'aulapython@yahoo.com'
ya_password='wrvbvrpbtqerbxqy'

#Gmail
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password=password)
    connection.sendmail(from_addr=my_email, 
    to_addrs='aulapython@yahoo.com', 
    msg="Subject:Gmail Code\n\nThis is the body of my email(Gmail)")

#Yahoo
with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user= ya_email, password=ya_password)
    connection.sendmail(from_addr=ya_email, 
    to_addrs= my_email, 
    msg="Subject:Yahoo Code\n\nThis is the body of my email(Yahoo)")