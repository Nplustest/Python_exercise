#! python3
# Saves and loads pieces of text to the clipboard.
#Usage: py.exe 8_6.pyw save <keyword> - Saves clipboard to keyword.
#		py.exe 8_6.pyw <keyword> - Loads keyword to clipboard.
#		py.exe 8_6.pyw list - Loads all keyword to clipboard.

import shelve,pyperclip,sys

mcbShelf = shelve.open('mcb')
#Save clipboard content.
if len(sys.argv) == 2 and sys.argv[1].lower == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 1:
	if sys.argv[1].lower() == 'list':
		mcbShelf.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()