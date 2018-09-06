#!/usr/bin/python3
# description     : This script automates entering reports at the end
#				   of the shift from a file to a web page. It also ends shift and closes open browsers
# author		     : Florin Badea for SiteGround
# date            : 15.10.2017
# usage		     : ./endshift.py or create a bash alias
#				   (adding shutdown -h now shuts down system too)
# requirements    : download the Linux chromedriver @ https://sites.google.com/a/chromium.org/chromedriver/downloads
#                  copy the chromedriver binary to /usr/bin
# FOR SPECIAL CHARACTERS USE https://meyerweb.com/eric/tools/dencoder/ TO ENCODE/DECODE				
# ========================================================================================

import os
import time
import pyautogui
from selenium import webdriver

today = time.strftime("%d.%m.%Y")
reportFilePath = '/path/to/file.txt'
reportsPassword = input("Forum password: ") 

# focus chrome browser
#pyautogui.click(800, 1065)
# focus the helpdesk window
#pyautogui.click(2016, 0)

# scroll up
#pyautogui.press('pageup')
#pyautogui.press('pageup')

# click the SiteGround logo to go to the homepage
#pyautogui.click(2051, 148)
# wait for the page to load
#time.sleep(5)
# click end shift
#pyautogui.click(2997, 164)
#time.sleep(2)
# click the dialog box
#pyautogui.click(3039, 161)

#time.sleep(3)
# close the browser
#pyautogui.click(3824, 10)
#time.sleep(3)
#pyautogui.click(1904, 14)

# start webdriver and submitting reports procedure
driver = webdriver.Chrome()

# open the page with basic HTTP authentcation (https://user@pass:reportspage.tld)
driver.get("https://USER:"+reportsPassword+"@URL")
# open the forum login page
driver.get("https://URL")

# find user and pass fields on the page and store them in variables
usernameElem = driver.find_element_by_id('username')
passwordElem = driver.find_element_by_id('password')

# send the authentications to the user and pass fields
usernameElem.send_keys('$USER')
passwordElem.send_keys('$PASS')

# find the login button and click (login)
driver.find_element_by_name('login').click()

# go to Lubo's report's page
driver.get("URL")
# enter submit new thread on the forum
driver.get("URL")

# find the subject and message fields in the page
subjectElem = driver.find_element_by_id("subject")
messageElem = driver.find_element_by_id("message")

# enter the subject
subjectElem.send_keys('Report - Florin B - ', today)

# open the report file
reportFile = open(reportFilePath, 'r')

# iterate over each line of the report file and fill in the message body
for line in reportFile.readlines():
	messageElem.send_keys(line)

# close the file
reportFile.close()

# click submit
driver.find_element_by_name('post').click()

# wait 3 seconds
time.sleep(3)

# close the browser
driver.quit()
