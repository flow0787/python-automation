#!/usr/bin/python
# Description     : This automates the process of transferring a site's files and folders via FTP
# Usage           : ./ftp.py
#                 : TO BE RUN INSIDE THE USER'S HOME
#---------------------------------------------------------------------------------#
# Author		      : Florin Badea
# Source		      : https://github.com/flow0787/python-automation
#---------------------------------------------------------------------------------#
# Date            : 06-09-2018
# Updated         : -
# Requirements    : wget + python 2.x
# References      : N/A
#=================================================================================#

import os
import time
import sys

#clear terminal screen
os.system("clear")


print("-=====BEGIN FTP SITE TRANSFER=====-")


#Test if transfer folder exists and start downloading
if os.path.exists("transfer"):
  print("Transfer directory already exists:")
  os.listdir("transfer")
  sys.exit("Exitting ...")
  
else:
  os.mkdir("transfer")
  os.chdir("transfer")
  ftp_user = raw_input("FTP user: ")
  ftp_pass = raw_input("FTP pass: ")
  ftp_host = raw_input("FTP host (IP/PATH): ")
  print("-=====  END CREDENTIALS  =====-")
  os.system("wget -mb --passive-ftp --ftp-user=%s --ftp-password=%s ftp://%s" % (ftp_user, ftp_pass, ftp_host))


#Wait 3 seconds
time.sleep(3)

#Check if download went well
if os.path.exists("wget-log"):
  print("Transfer is now in progress: ")
  file_object = open("wget-log", "r")
  for line in file_object:
    if "saved" in line:
      print(line)
  print("-=====END FTP SITE TRANSFER=====-")
else:
  print("Issued detected:")
  file_object = open("wget-log", "r")
  file_object.readlines(10)
  print("-=====END FTP SITE TRANSFER=====-")

print("""
  Check progress by running:
  tail ~$user/transfer/wget-log\n
  \t-=====Next Steps=====-
  1. Transfer Database (can use https://www.adminer.org/ if no control panel access)
  2. Move site files & folders / Add domain on the account (if needed)
  3. Import Database & adjust database connection files"
  """)