__author__ = 'akshay'
import smtplib
from email.mime.text import MIMEText


class EmailService:
    def sendForUser(self, user, subject, message):
        message = 'Hi ' + user.name + '!\n' + message
        self.send(user.emailId, subject, message)

    def send(self, emailId, subject, message):
        fromaddr = 'akshay#####'
        toaddrs = [emailId]

        msg = MIMEText(message)
        msg['Subject'] = subject

        # Credentials (if needed)
        username = 'akshay#####'
        password = '######'

        # The actual mail send
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()
