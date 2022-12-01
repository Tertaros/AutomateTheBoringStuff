#! python3
# Walks through a folder three and searches files with a specific extension.
# Copies found files to the a new folder

import shutil, os, sys, pyperclip
from pathlib import Path


#Request directory to investigate
print('Please provide the path for the folder you wish to investigate.')
searchPathText = input()
if(searchPathText == 'copy'):
    searchPathText = pyperclip.paste()
searchPath = Path(searchPathText)
print(searchPath)
#Check if provided directory exists
if(searchPath.is_dir() == False):
    print('Provided directory does not exist. \n The programm will be aborted')
    sys.exit()

print('Please provide provide the file extension you want to look for e.g. "txt"')
fileExt = input()

print(f'Please provide the path for the folder you wish to copy all the {fileExt} to. ')
targetPathText = input()
if(targetPathText == 'copy'):
    targetPathText = pyperclip.paste()
targetPath = Path(targetPathText)
print(targetPath)


#tree = list(searchPath.glob(str('*.'+fileExt))) Does not search within folders recursively
tree = os.walk(searchPath)

for folderName, subfolders, filenames in tree:

    for filename in filenames:
        if filename.endswith("."+fileExt):

            print(folderName + '\\' +filename)
            print(targetPathText + '\\' +filename)
            shutil.copy(str(folderName + '\\' +filename),str(targetPathText + '\\' +filename))




