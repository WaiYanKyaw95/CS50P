# importing the required libraries
import sys
import random
from pyfiglet import Figlet

# to use the figlet library and get the list of fonts from the library
figlet = Figlet()
fontList = figlet.getFonts()

# ensure that the program expects zero or two command-line args
# and first arg must be -f or --font
# second arg must be the name of the font from the font list
if len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in fontList:
    # choose the font from user input
    choosenFont = sys.argv[2]

# if zero arg, then random font must be applied using random library
elif len(sys.argv) == 1:
    choosenFont = random.choice(fontList)

else:
    sys.exit("Invalid usage")

# set the font
figlet.setFont(font=choosenFont)

# asking for user's input and printing it out
text = input("Input: ")
print(figlet.renderText(text))