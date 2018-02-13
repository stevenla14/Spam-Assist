#!/usr/bin/python
import random, sys, smtplib, getpass, os

domain_names = {'gmail': 'smtp.gmail.com', 'outlook': 'smtp-mail.outlook.com', 'hotmail': 'smtp-mail.outlook.com', 'yahoo': 'smtp.mail.yahoo.com', 'at&t': 'smpt.mail.att.net', 'comcast': 'smtp.comcast.net', 'verizon': 'smtp.verizon.net'}

print('Who is your email provider? (Gmail, Yahoo, AT&T, etc.)')
provider = (input()).lower()

while not provider in domain_names.keys():
    print('Invalid provider!\nWho is your email provider? (Gmail, Yahoo, AT&T, etc.)')
    provider = (input()).lower()

print('What is your email ID?')
email_ID = input()

print ('What is your email extension? (.com, .edu, etc.)')
extension = input()

password = getpass.getpass(prompt='What is your email password?\n')

full_email = email_ID + '@' + provider + extension
smtpObj = None

if (provider == 'at&t') or (provider == 'verizon'):
    smtpObj = smtplib.SMTP_SSL(domain_names[provider], 465)
    smtpObj.ehlo()
else:
    smtpObj = smtplib.SMTP(domain_names[provider], 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    
smtpObj.login(full_email, password)

print('What is the name of the file containing all of the emails? (Include extension)')
input_file = input()
input_fileObj = open(input_file, 'r')
temp = input_fileObj.readlines()

input_list = []
for i in temp:
    if i != '\n':
        input_list.append(i.strip())

print('What is the name of the file containing the spam message? (Include extension)')
message_file = input()
message_fileObj = open(message_file, 'r')
message_content = message_fileObj.read()

print('Enter the subject for the email:')
subject = input()

# counter stuff...
counter = 1
for i in input_list:
    recipient = i
    # counter ...
    adjusted_subject = 'Subject: ' + subject + ' (' + str(counter) + ')' + '\n'
    message = message_content.replace('\\n', '\n')
    smtpObj.sendmail(full_email, recipient, adjusted_subject + message)
    # counter ...
    counter += 1

smtpObj.quit()
if not input_list:
    print('Nothing was sent, since your file containing all of the emails is empty!')
else:
    print('Success! Your email(s) have been sent.')
