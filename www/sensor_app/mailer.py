import smtplib
import os
from email.message import EmailMessage
from email.headerregistry import Address

mail_password = os.environ.get('RPI_MAIL_GOOGLE_PASS')
mail_user = os.environ.get('MY_MAIL_ADR')
mail_receiver = os.environ.get('MAIL_ADR')

def send(temp, humid):
    msg = EmailMessage()
    msg['Subject'] = "Automated temperature alert"
    msg['From'] = Address("RPI-server", "humitemp", mail_user)
    msg['To'] = (mail_receiver)
    msg.set_content("""\
    <html>
      <head></head>
      <body>
        <p>This is an automated alert service.</p>
        <p>the current temperature is out of optimal range.</p>
        <p>temperature is {}, optimally you want to stay under 26c<p/>
        <p>humidity is {}, higher temps benefit from higher humidity<p/>
      </body>
    </html>
    """.format(temp, humid), subtype='html')

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(user=mail_user, password=mail_password)
        smtp.send_message(msg)

