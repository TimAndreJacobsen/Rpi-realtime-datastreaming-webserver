import smtplib
import os

mail_password = os.environ.get('RPI_MAIL_GOOGLE_PASS')
mail_user = os.environ.get('MY_MAIL_ADR')
mail_receiver = os.environ.get('MAIL_ADR')

def send(temp, humid):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(user=mail_user, password=mail_password)

        subject = 'subject goes here'
        body = 'temperature is {}\nhumidity is {}'.format(temp, humid)

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(mail_user, mail_user, msg)
