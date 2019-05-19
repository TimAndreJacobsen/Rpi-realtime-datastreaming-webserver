import smtplib
import os

mail_password = os.environ.get('RPI_MAIL_GOOGLE_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()