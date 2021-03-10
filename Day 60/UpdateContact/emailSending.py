import smtplib

email_sender = "########@gmail.com"
password = "######################"

def sending(name, phoneNumber, email, message):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(email_sender, password)
        connection.sendmail(from_addr=email_sender,
                            to_addrs="einoyakoreal@gmail.com",
                            msg=f"Subject: Email Report \n\nName: {name}\nEmail: {email}\nPhone Number:{phoneNumber}\nMessage:{message}")