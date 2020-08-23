# Snapshots on Mac automatically save to the desktop which makes my desktop very messy and I'm sick of it. This program will search my desktop for these screenshots and move them to a screenshot folder on my desktop. I am going to keep it realatively general so it should work on MacOS or Windows (not sure where screenshots on Windows are stored...)

# DONE Define Problem and Necessary Components and make more todos based on that
# Need to adjust startup script based on where you store this script
# TIME: 1 Day to complete

# import os, shutil, and othe libraries
import os
import shutil
import re

# set up a path to screen shot folder (this is on my desktop)
path_screenshot_folder = os.path.expanduser("~/Desktop/screenshots")

# Navigate to desktop with os
os.chdir(os.path.expanduser("~/Desktop"))

# Read in all file names
desktop_list = os.listdir()

# Screen shots are always saved in the following format: Screen Shot ####-##-## at 4.59.51 (AM/PM)
# I will only look for the first two words "Screen shots" since this is already pretty uncommon
screen_shot_pattern = re.compile('Screen Shot')

# This list will hold file names of screen shots on desktop
screen_shot_list = []

# Iterates through all files on desktop and if 'Screen Shot' is in name it is added to the screen shot list
# I realize regex is overkill here but as my projects get more complex I want to be used to using it
for file_name in desktop_list:
    if(re.search(screen_shot_pattern,file_name)):
        screen_shot_list.append(file_name)

# We can now use shutil to move these files to a screenshot folder. This could have been done in the previous loop but this is more readable
for screen_shot in screen_shot_list:
    print(f"Moving {screen_shot}")
    shutil.move(os.getcwd()+ '/'+ screen_shot, path_screenshot_folder)
