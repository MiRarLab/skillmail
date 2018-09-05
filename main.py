
import smtplib
import getpass
from email import encoders
from email.mime.base import MIMEBase
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

def attachment(msg):
    filename = input("Name of the file and extension: ")
    attachment = open(input("Path of the file: "), "rb")
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    
    msg.attach(part)
    return msg

def send(msg, smtp_obj):
    ''' Send the email and quit the SMPP '''

    smtp_obj.sendmail(msg['from'], msg['to'], msg.as_string())
    smtp_obj.quit()
 
    print(f"Successfully sent email to {msg['to']}")

def main():
    with_attach = input("Send email with attachment True or False: ")
    msg, password, message = enter()
    smtp_obj = configure(msg, message, password)
    if  with_attach.lower() == "true": msg = attachment(msg)
  
    send(msg, smtp_obj)

if __name__ == "__main__":
    main()
