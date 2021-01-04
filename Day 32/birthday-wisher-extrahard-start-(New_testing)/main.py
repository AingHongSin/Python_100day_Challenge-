import datetime as dt
import random
import smtplib
import pandas

now = dt.datetime.now()
THIS_MONTH =now.month
TODAY = now.day
SENDER = 'einoyakoreal@gmail.com'
PASSWORD = 'Ainghongsin'
PERSONAL_BIRTH = (THIS_MONTH, TODAY)

first_minute = now.minute
first_sec = now.second

##################### Extra Hard Starting Project ######################

csv_data = pandas.read_csv('birthdays.csv')


Birthday_dist = {(data_row['month'], data_row['day']): data_row for (index, data_row) in csv_data.iterrows()}

# print("\n\nBirthday_Dist: ",Birthday_dist)
#
# print(len(Birthday_dist[THIS_MONTH, TODAY]))
n = 0

# 2. Check if today matches a birthday in the birthdays.csv
while n < 20:
    # if int((csv_data[csv_data['month'] == THIS_MONTH]).month) == THIS_MONTH and int((csv_data[csv_data['day'] == TODAY]).day) == TODAY:
    if (THIS_MONTH, TODAY) in Birthday_dist:
        birth = Birthday_dist[PERSONAL_BIRTH]
        NAME = (birth['name'])
        # print("NAME: ", NAME)
        SEND_TO_EMAIL = birth['email']

        # print("SEND TO EMAIL: ", SEND_TO_EMAIL)

         # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        # letter_template_list = ['letter_1.txt','letter_2.txt','letter_2.txt']
        # letter_template = random.choice(letter_template_list)

        path_file = (f"./letter_templates/letter_{random.randint(1,3)}.txt")
        with open(path_file) as file:
            data = file.read()
        MESSAGE = data.replace("[NAME]", NAME)
        # print(f"\n\n\n\n{MESSAGE}\n\n\n\n" )

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(SENDER, PASSWORD)

            connection.sendmail(from_addr=SENDER, to_addrs=SEND_TO_EMAIL, msg = (f"Subject:Happy Birthday\n\n{MESSAGE}"))


    print(f"Message have been sent in {n} time")

    n += 1
second = now.minute
sec_secone = now.second

print(f"Result:{first_minute - second_minute}m : {sec_secone - first_sec}s")

print('\nCode Completed\n')

