import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import numpy as np


def send_mail(fromaddr, toaddr, password, subject, body, file_name):

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = subject

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    attachment = open(file_name, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % file_name)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


def main():
    if len(sys.argv) < 3:
        print("Please provide mail address and password.")
        return

    fromaddr = sys.argv[1]
    toaddr = sys.argv[1]

    # Get the password
    password = sys.argv[2]
    subject = "Home Report"
    body = "Hello Ivan, \n Here are your results:\n"

    results = np.genfromtxt("site_full.txt", dtype="str")
    # Append files and results
    for i in results:
        body += i[0] + " " + i[1] + "\n\n"

    body += "\nSincerely,\n Friendly Neighborhood Spam Bot Prevention Bot"
    send_mail(fromaddr, toaddr, password, subject, body, "results.txt")


if __name__ == "__main__":
    main()
