#!/usr/bin/python3
# description     : This script automates accessing cPanel and creating a backup
# author		      : Florin Badea for SiteGround
# date            : 15.10.2017
# usage		        : ./cpanel_migrator.py
# requirements    : download the Linux chromedriver @ https://sites.google.com/a/chromium.org/chromedriver/downloads
#                   copy the chromedriver binary to /usr/bin
# ===================================================================================================================

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

cPanelUser = input("User: ")
cPanelPass = input("Pass: ")

# start webdriver and submitting reports procedure
browser = webdriver.Chrome()

# open the cPanel page
browser.get("https://my.bluehost.com/hosting/cpanel")

# wait for the page to load
browser.implicitly_wait(30)

# find user and pass fields on the page and store them in variables
userField = browser.find_element_by_id('ldomain')
passField = browser.find_element_by_id('lpass')

# send the authentications to the user and pass fields
userField.send_keys(cPanelUser)
passField.send_keys(cPanelPass)

# find the login button and click (login)
browser.find_element_by_class_name("btn_secondary").click()
time.sleep(5)

# go to the cpanel page
browser.find_element_by_xpath('//a[@href="/cgi/cpanel"]').click()
time.sleep(5)


# print the statistics
stats = []
for i in browser.find_elements_by_id("stats_section"):
	stats.append(i.text.split("\n"))
# print the stats on their own line
print("cPanel account statistics:", '\n')
for j in stats:
	print("\n".join(j))


# go to the disk space usage page
browser.find_element_by_xpath('//a[@href="/web-hosting/cplogin?goto_uri=/frontend/bluehost/diskusage/index.html"]').click()
time.sleep(5)
diskUsed = browser.find_element_by_xpath("//div[@class='total'][1]").text
print('\n', diskUsed, '\n')

# get new URL
URL = browser.current_url
newURL = URL.split("diskusage")[0]


# go to the backup page and generate the backup
browser.get(newURL + "backup/wizard-fullbackup.html")
radioEmail = browser.find_element_by_xpath("(//input[@type='radio'][@name='email_radio'])[1]")

if radioEmail.is_selected():
	# find and fill the email notification
	emailField = browser.find_element_by_id("backup_email")
	emailField.send_keys(Keys.CONTROL + "a")
	emailField.send_keys(Keys.DELETE)
	emailField.send_keys("florin.badea@siteground.com")
	# find and click the "Generate Backup" button
	generateBackupButton = browser.find_element_by_id("backup_submit")
	generateBackupButton.click()
else:

	radioEmail.click()
	# find and fill the email notification
	emailField = browser.find_element_by_id("backup_email")
	emailField.send_keys(Keys.CONTROL + "a")
	emailField.send_keys(Keys.DELETE)
	emailField.send_keys("plovdiv@siteground.com")
	# find and click the "Generate Backup" button
	generateBackupButton = browser.find_element_by_id("backup_submit")
	generateBackupButton.click()


