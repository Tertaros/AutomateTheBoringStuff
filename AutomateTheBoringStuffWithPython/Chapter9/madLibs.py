# Madlibs

# Create a Mad Libs program that reads in text files and lets the user add their own tex
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.


from pathlib import Path
import re, sys

defaultText = 'The ADJECTIVE NOUN walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
checklist = ('noun','verb','adjective')

#Determine file to read
print('Which file do you want to read?')
print('Please provide a relative path to the current working directory.')
print('Current working directory: ' + str(Path.cwd()))
inputPathText = input()
inputPath = Path(Path.cwd() / inputPathText)
print(inputPath)

#Check if file exists
if inputPath.is_file() == False:
    print('File does not exist.')
    print('Input "CANCEL" in case you want to stop otherwise a new file with the following default text will be created:')
    print(defaultText)
    #Cancel option
    fileNotExists = input()
    if(fileNotExists.lower() == 'cancel'):
        print('Programm reached cancel')
        sys.exit()
    #Create new file
    else:
        file = open(inputPath,'w')
        file.write(defaultText)
        file.close()

#Open File
mlFile = open(inputPath)
mlFileContent = mlFile.read()

# Go over each word and check if it needs to be replaced
replacementCount = 0
for word in re.split('\W+',mlFileContent): #Initially used string.split() but that did not work with punctuation like "VERB."
    if word.lower() in checklist:
        print('Enter ' + word.lower())
        newWord = input()
        mlFileContent = mlFileContent.replace(word,newWord,1)
        replacementCount+=1

# If no word is replaced, exit
if replacementCount == 0:
    print('No words found to replace. \n Process will be aborted.')
    mlFile.close()
    sys.exit()

#Write new text in result file
resultFile = open('result.txt', "w")
resultFile.write(mlFileContent)
resultFile.close()
print(mlFileContent)

print('Programm reached end')




