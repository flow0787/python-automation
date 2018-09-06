
#description     : This script automates entering reports at the end 
#				   of the shift from a file to a web page.
#author		     : Florin Badea for SiteGround
#date            : 15.10.2017
#usage		     : python3 report_automationMAC.py or create a bash alias 
#				   (adding shutdown -h now shuts down system too)
#requirements    : download the MAC chromedriver @ https://sites.google.com/a/chromium.org/chromedriver/downloads
#                  copy the chromedriver binary to /usr/local/bin/
#=============================================================================

import os
import time
from selenium import webdriver

today = time.strftime("%d.%m.%Y")
reportFilePath = '/path/to/file.txt'


driver = webdriver.Chrome()
#open the page with basic HTTP authentcation (https://user@pass:reportspage.tld)
driver.get("https://$USERL$PASS@URL_HERE")
#open the forum login page
driver.get("LOGIN_URL")

#find user and pass fields on the page and store them in variables
usernameElem = driver.find_element_by_id('username')
passwordElem = driver.find_element_by_id('password')

#send the authentications to the user and pass fields
#TOD: 
# GET USER
# GET PASS
#find the login button and click (login)
driver.find_element_by_name('login').click()

#go to Dimitar's report's page
driver.get("DIMITAR_PAGE")
#enter submit new thread on the forum
driver.get("HIT SUBMIT")


#find the subject and message fields in the page
subjectElem = driver.find_element_by_id("subject")
messageElem = driver.find_element_by_id("message")

#enter the subject
subjectElem.send_keys('Report - Florin B - ',today)

#open the report file
reportFile = open(reportFilePath,'r')

#iterate over each line of the report file and fill in the message body
for line in reportFile.readlines():
	messageElem.send_keys(line)

#close the file 
reportFile.close()

#click submit
driver.find_element_by_name('post').click()

#wait 3 seconds
time.sleep(3)

#close the browser
driver.quit()
