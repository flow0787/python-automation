#!/usr/bin/python
# Description     : A python script that automates multiple email account transfers 
#                   using the imapsync tool
# Usage           : ./imapsync.py
#---------------------------------------------------------------------------------#
# Author		      : Florin Badea
# Source		      : https://github.com/flow0787/python-automation
#---------------------------------------------------------------------------------#
# Date            : 03-09-2018
# Updated         : 06-09-2018
# Requirements    : python 2.7+ and imapsync
# References      : N/A
#=================================================================================#

import subprocess

fromHost = raw_input("From Host: ")
toHost = raw_input("To Host: ")
emails = []
passwords = []
emailsToSync = {}

while (True):
  email = raw_input("Email: ")
  emails.append(email)

  ass = raw_input("Pass: ")
  passwords.append(ass)

  emailsToSync = dict(zip(emails, passwords))

  finished = raw_input("Finished? y/n ")

  if finished.lower() == "y":
    break

for emails, passwords in emailsToSync.items():
  #if email1=email2 and pass1=pass2 run:
  #os.system("imapsync --host1 %s --user1 %s --password1 '%s' --host2 %s --user2 %s --password2 '%s' --ssl1 --no-modulesversion --ssl2" % (fromHost, emails, passwords, toHost, emails, passwords))
  args = [
    "imapsync",
    "--host1",
    fromHost,
    "--user1",
    emails,
    "--password1",
    "'\"{}\"'".format(passwords),
    "--host2",
    toHost,
    "--user2",
    emails,
    "--password2",
    "'\"{}\"'".format(passwords),
    "--ssl1",
    "--no-modulesversion",
    "--ssl2"
  ]
  p = subprocess.Popen(args, stdout=subprocess.PIPE)
  output, errors = p.communicate()
  print(output)
