#! python3
# Walk through to a folder and search for large files
# Delete those large files
# Deleted files are printed with their absolute path

import os, sys, pyperclip, re, math, send2trash
from pathlib import Path

# Request directory to walk through
print('Please provide a path to the target directory you with to investigate. \nType in "copy" if you want to use the value from the clipboard.')
searchPathText = input()

# Check if copy was typed and if so
if(searchPathText == 'copy'):
    searchPathText = pyperclip.paste()
searchPath = Path(searchPathText)
print(searchPath)

# Check if provided directory does exists, if not exit program
if (searchPath.is_dir() == False):
    print('Provided directory does not exist.\nThe Program will be aborted.')
    sys.exit()

# Allowing users to input their own treshold in MB
print('Please provide a numeric treshold at which size files in the target directory should be deleted in MB.\nIf no value is provided 100MB as value will be used.')
tresholdText = input()

# Checking with regex if input is float or int and therefore valid
int_regex = re.compile('^[0-9]*$')
float_regex = re.compile('^[0-9]*.[0-9]*$')
isInt = int_regex.match(tresholdText)
isFloat = float_regex.match(tresholdText)

if isInt == False and isFloat == False:
    print('Provided value is not a valid numeric value.\nThe program will be aborted.')
    sys.exit()

# Converintg string to float
# Any int should also be convertible to a float
treshold= float(tresholdText)

#Walk the directory
tree = os.walk(searchPath)
for foldername, subfolders, filenames in tree:
    for filename in filenames:
        #Get File Size
        fileSize = os.path.getsize(foldername +'\\'+ filename)
        # Converting file size into MB, 1 MB = 1024 KB -> 1 KB = 1024 B
        fileSizeMB = round(fileSize / math.pow(1024,2), 3)
        if(fileSizeMB>=treshold):
            print('File size of '+foldername + filename + ': '+ str(fileSizeMB) + 'MB\nDeleted!')
            # Deleting files with Send2Trash to allow recovery | KEEP commented
            #send2trash.send2trash(foldername + '\\' + filename)

print('Program concluded')
