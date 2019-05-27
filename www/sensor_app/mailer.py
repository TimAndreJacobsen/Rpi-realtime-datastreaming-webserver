import smtplib
import os
from email.message import EmailMessage
from email.headerregistry import Address

mail_password = os.environ.get('RPI_MAIL_GOOGLE_PASS')
mail_user = os.environ.get('MY_MAIL_ADR')
mail_receiver = os.environ.get('MAIL_ADR')

def send(temp, humid):
    msg = EmailMessage()
    msg['Subject'] = "Ayons asperges pour le déjeuner"
    msg['From'] = Address("RPI-server", "humitemp", mail_user)
    msg['To'] = (mail_receiver)
    msg.set_content("""\
    This is an automated alert service.
    the current temperature is out of optimal range.
    temperature is {}, optimally you want to stay under 26c
    humidity is {}, higher temps benefit from higher humidity
    """.format(temp, humid))

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(user=mail_user, password=mail_password)
        smtp.send_message(msg)

