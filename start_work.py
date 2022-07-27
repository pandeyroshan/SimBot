import os
import pyautogui
import time

def clickTheWorkspace():
    pyautogui.click(30,300)
    clickTheChrome()
    pass

def fillPasswordInWorkspaceAndLogin():
    pass

def clickTheChrome():
    pyautogui.click(30,70)
    time.sleep(3)
    pyautogui.click(880,550)
    pass

def openTheAttendanceBookmark():
    pass

def markTheAttendance():
    pass

def dateInformer():
    pass

def startTheWheel():
    title = "START"
    message = "Let the work begin"
    os.system('notify-send "{}" "{}"'.format(title, message))
    clickTheWorkspace()
    pass

if __name__ == '__main__':
    time.sleep(2)
    startTheWheel()
"""
TODO

1) Say out loud the day with how many days left in this month and how many days has till spent with coditas
2) Do the Affirmation, Solitude
3) Open up the browser and mark the attendance
4) open up the AWS workspace
"""