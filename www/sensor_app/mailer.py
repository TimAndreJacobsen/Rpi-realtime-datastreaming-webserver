import smtplib
import os

mail_password = os.environ.get('RPI_MAIL_GOOGLE_PASS')
mail_user = 'tymmyh@gmail.com'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(user=mail_user, password=mail_password)
