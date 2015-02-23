#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import sys

if len(sys.argv) < 2:
    print('usage: {script} file-to-send.html'.format(script = sys.argv[0]),
          file = sys.stderr)
    exit(1)

print('File: ' + sys.argv[1])
usr = input('GMail User: ')
pwd = getpass.getpass()
title = input('Title: ')
to = input('To: ')

print('From: {usr}@gmail.com'.format(usr = usr))
print('To: {to}'.format(to = to.split(',')))
print('Title: {title}'.format(title = title))

ans = input('Continue? (y)').strip()
if ans and (ans != 'y' or ans != 'Y'):
    print('Abort.')
    exit(0)


message = MIMEMultipart()
html = open(sys.argv[1]).read()
body = MIMEText(html, 'html')


message['From'] = '{0} <{0}@gmail.com>'.format(usr)
message['To'] = to
message['Subject'] = title

message.attach(body)

msg_full = message.as_string()

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(usr, pwd)
server.sendmail(usr + '@gmail.com',
                [ r.strip() for r in to.split(',') ],
                msg_full)
server.quit()
