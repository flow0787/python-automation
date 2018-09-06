#!/usr/bin/python3
# description     : This script automates accessing cPanel and creating a backup
# author		      : Florin Badea for SiteGround
# date            : 15.10.2017
# usage		        : ./cpanel_migrator.py
# requirements    : download the Linux chromedriver @ https://sites.google.com/a/chromium.org/chromedriver/downloads
#                   copy the chromedriver binary to /usr/bin
# ===================================================================================================================

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ask for cPanel details
cPanelUrl = input("cPanel: ")
cPanelUser = input("User: ")
cPanelPass = input("Pass: ")

# start webdriver and submitting reports procedure
browser = webdriver.Chrome()

# open the cPanel page
browser.get("http://"+ cPanelUrl + ":2082")

# wait for the page to load
browser.implicitly_wait(30)

if "bluehost.com" in browser.current_url:
	# find user and pass fields on the page and store them in variables
	userField = browser.find_element_by_id('ldomain')
	passField = browser.find_element_by_id('lpass')
else:
	# find user and pass fields on the page and store them in variables
	userField = browser.find_element_by_id('user')
	passField = browser.find_element_by_id('pass')

# send the authentications to the user and pass fields
userField.send_keys(cPanelUser)
passField.send_keys(cPanelPass)

if "bluehost.com" in browser.current_url:
	# find the login button and click (login)
	browser.find_element_by_class_name("btn_secondary").click()
else:
	# find the login button and click (login)
	browser.find_element_by_id('login_submit').click()

time.sleep(5)

# get the newly generated cPanel URL after login
URL = browser.current_url


# get stats function
def get_stats():

	# if it is a SiteGround cPanel account OR if cPanel runs with paper_lantern theme
	if "index.php" in URL and "Crystal" in URL or "paper_lantern" in URL:
		stats = []
		for i in browser.find_elements_by_id("stats"):
			stats.append(i.text.split("\n"))
		# print the stats on their own line
		print("cPanel account statistics:", '\n')
		for j in stats:
			print("\n".join(j))

	# if cPanel runs with x3 theme
	elif "index.html" in URL and "x3" in URL:
			stats = []
			for i in browser.find_elements_by_id("content-stats"):
				stats.append(i.text.split("\n"))
			# print the stats on their own line
			print("cPanel account statistics:", '\n')
			for j in stats:
				print("\n".join(j))
	# if it is a BlueHost cPanel account
	elif "bluehost.com" in URL:
			stats = []
			for i in browser.find_elements_by_id("stats_section"):
				stats.append(i.text.split("\n"))
			# print the stats on their own line
			print("cPanel account statistics:", '\n')
			for j in stats:
				print("\n".join(j))


def get_diskusage():

	if "bluehost.com" in browser.current_url:
		# go to the disk space usage page
		browser.find_element_by_xpath(
			'//a[@href="/web-hosting/cplogin?goto_uri=/frontend/bluehost/diskusage/index.html"]').click()
		diskUsed = browser.find_element_by_xpath("//div[@class='total'][1]").text
		print('\n', diskUsed, '\n')

	elif "index.php" in URL and "Crystal" in URL:
		newcPanelURL = URL.split("index.php")[0]
		# go to the disk usage page and print the disk used
		browser.get(newcPanelURL + "diskusage/index.html")
		diskUsed = browser.find_element_by_xpath("//div[@class='total'][1]").text
		print('\n', diskUsed, '\n')
	else:
		newcPanelURL = URL.split("index.html")[0]
		# go to the disk usage page and print the disk used
		browser.get(newcPanelURL + "diskusage/index.html")
		diskUsed = browser.find_element_by_xpath("//div[@class='total'][1]").text
		print('\n', diskUsed, '\n')


def generate_backup():

	if "bluehost.com" in URL:
		# get new URL
		newURL = browser.current_url.split("diskusage")[0]
		# go to the backup page and generate the backup
		browser.get(newURL + "backup/wizard-fullbackup.html")
		do_backup()

	elif "index.php" in browser.current_url and "Crystal" in URL:
			newcPanelURL = URL.split("index.php")[0]
			# go to the backup page
			browser.get(newcPanelURL + "backup/wizard-fullbackup.html")
	elif "index.html" in URL:
			newcPanelURL = URL.split("index.html")[0]
			# go to the backup page
			browser.get(newcPanelURL + "backup/wizard-fullbackup.html")
			do_backup()

def do_backup():

	radioEmail = browser.find_element_by_xpath("(//input[@type='radio'][@name='email_radio'])[1]")
	# generate backup
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


def quit():

	input("Press any key to quit...")
	browser.quit()


def proceed():

	choice = input("Continue with generating backup (y/n)? ")
	if choice.lower() == "y":
		print("Generating backup...", '\n')
		generate_backup()
	else:
		sys.exit(0)

def main_script():

	# if it is a SiteGround cPanel account
	if "index.php" in URL and "Crystal" in URL:
		get_stats()
		get_diskusage()
		proceed()
		quit()

	# if cPanel runs with x3 theme
	elif "index.html" in URL and "x3" in URL:
		get_stats()
		get_diskusage()
		proceed()
		quit()

	# if cPanel runs with paper_lantern theme
	elif "index.html" in URL and "paper_lantern" in URL:
		get_stats()
		get_diskusage()
		proceed()
		quit()

	# if it is a BlueHost cPanel account
	elif "bluehost.com" in URL:
		# go to the cpanel page
		#browser.find_element_by_xpath('//a[@href="/cgi/cpanel"]').click()
		get_stats()
		get_diskusage()
		proceed()
		quit()

	# not sure if this should stay here...
	elif "index.html" in URL:
		get_stats()
		get_diskusage()
		proceed()
		quit()

	else:
		print("No recognizable cPanel URL or login failed!", '\n')


main_script()