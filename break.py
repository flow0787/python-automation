#!/usr/bin/python3
#description     : This script automates the breaks on shift
#author		     : Florin Badea for SiteGround
#date            : 18.10.2017
#usage		     : ./break.py $NO where $NO is the time you wish to break for
#requirements    : install pip3 and pyautogui
#=============================================================================

import time
import pyautogui
import sys
import datetime

breakTime = int(sys.argv[1])
now       = datetime.datetime.now()
diff      = datetime.timedelta(seconds=breakTime*60)
beBackAt  = now + diff


print("Starting break for {} min.".format(breakTime))
#print time at the break start and when to be back
#print("Current time is: {}".format(time.strftime('%X %x %Z')))
print("Current time is: {}".format(now.strftime('%H:%M:%S')), '\n')
print("Be back at: {}".format(beBackAt.strftime('%H:%M:%S')), '\n')
#focus chrome browser
pyautogui.click(800, 1065)
#focus the helpdesk window
pyautogui.click(2016, 0)

#scroll up
pyautogui.press('pageup')
pyautogui.press('pageup')

#click the SiteGround logo to go to the homepage
#pyautogui.click(2051, 148)

#wait for the page to load
#time.sleep(3)
#click break
pyautogui.click(2997, 164)
time.sleep(2)
#click the dialog box
pyautogui.click(3039, 161)

#move mouse away from the break button
pyautogui.moveTo(2697, 515)

#wait for the amount of time passed as the argument (breakTime)
time.sleep(breakTime * 60)

#end break
pyautogui.click(2997, 164)
time.sleep(2)
pyautogui.click(3039, 161)


#move mouse away from the break button
pyautogui.moveTo(2697, 515)

print("{} min break ended.".format(breakTime))