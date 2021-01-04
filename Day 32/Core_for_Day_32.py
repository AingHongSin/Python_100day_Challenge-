# import smtplib
#
# my_email = 'ainghongsin9999@gmail.com'
# my_password = 'AINGHONGSIN9999'
# another_email = 'ainghongsin@yahoo.com'
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user = another_email, password = 'jveqxtonxgbvttsv')
#     connection.sendmail(from_addr= another_email, to_addrs=my_email, msg = 'Subject:Hello\n\nThis is the body of email ')


import datetime as dt

now = dt.datetime.now()
print(now.day)

date_of_birth = dt.datetime(year = 2002, month = 2, day = 7)
print(date_of_birth)