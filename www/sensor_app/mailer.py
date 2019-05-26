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
        html = """\
                <html>
                        <head></head>
                        <body>

                        </body>
                </html>
                """

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(mail_user, mail_user, msg)
