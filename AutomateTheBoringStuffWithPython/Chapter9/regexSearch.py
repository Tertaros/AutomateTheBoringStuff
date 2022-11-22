# Regex Search
# Opens all .txt files in a directory
# Seaches for any line that matches a user-supplied regular expression
# The result will be printed to the log

from pathlib import Path
import re, sys, pyperclip


print('Please provide the path for the folder you wish to investigate \n type in "copy" to grap the content in your clipboard')
inputPathText = input()
# If copy is input copy clipboard into input
if(inputPathText == 'copy'):
    inputPathText = pyperclip.paste()
inputPath = Path(inputPathText)
print(inputPath)

if(inputPath.is_dir() == False):
    print('Provided directory does not exist. \n The programm will be aborted')
    sys.exit()

#TESTING
#inputPath = Path.cwd()

print('Please provide a regular expression to use within the .txt files')
inputRegex = re.compile(input())

folder = list(inputPath.glob('*.txt'))
for filePath in folder:
    print(filePath)
    file = open(filePath)
    fileContent = file.readlines()
    for line in fileContent:
        searchResult = inputRegex.search(line)
        if(searchResult != None):
            print(searchResult.group())
    file.close()



