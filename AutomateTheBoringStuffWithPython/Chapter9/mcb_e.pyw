#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb_e.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb_e.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb_e.pyw list - Loads all keywords to clipboard.
#        py.exe mcb_e.pyw delete - Delete a keyword from the shelf.
#        py.exe mcb_e.pyw deleteAll - Deletes all the keywords

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")


if len(sys.argv) == 3:
    #Save clipboard content.
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    #Delete shelve content.
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    #List keywords and load content.
    if sys.argv[1].lower() == 'list':
        shelveList = list(mcbShelf.keys())
        if len(shelveList) == 0:
            pyperclip.copy('Shelve empty.')
        else:
            pyperclip.copy(str(shelveList))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'deleteall':
        mcbShelf.clear()


mcbShelf.close()
