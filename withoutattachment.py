import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def enter():
    ''' Function to get user input email-from/password/email-to/subject/message'''
    
    msg = MIMEMultipart()
    msg['from'] = input("Enter your email: ")
    password = getpass.getpass('Password: ')
    msg['to'] = input("Enter the email to: ")
    msg['subject'] = input("Subject: ")
    message = input("Message: ")

    return msg, password, message
 

def configure(msg, message, password):
    ''' Configure the SMTP object and login'''

    msg.attach(MIMEText(message, 'plain'))
    smtp_obj = smtplib.SMTP('smtp.gmail.com: 587')
    smtp_obj.starttls()
    smtp_obj.login(msg['from'], password)

    return smtp_obj
 
 
def send(msg, smtp_obj):
    ''' Send the email and quit the SMPT'''

    smtp_obj.sendmail(msg['from'], msg['to'], msg.as_string())
    smtp_obj.quit()
 
    print(f"Successfully sent email to {msg['to']}")


def main():
    msg, password, message = enter()
    smtp_obj = configure(msg, message, password)
    send(msg, smtp_obj)


if __name__ == "__main__":
    main()
