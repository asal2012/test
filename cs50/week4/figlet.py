from pyfiglet import Figlet
import random
import sys
figlet = Figlet()
font_list = figlet.getFonts()
if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == "--font":
        if sys.argv[2] in font_list:
            f = sys.argv[2]
        else:
            sys.exit("invalid font")
    else:
        sys.exit("first argument is invalid")
if len(sys.argv) == 2:
    sys.exit("an argument is less")
if len(sys.argv) == 1:
    f = random.choice(font_list)
text = input("Input: ")
figlet.setFont(font=f)
print(figlet.renderText(text))

# s = input("wright something: ")
# f = "slant"
# figlet.setFont(font=f)
# print(figlet.renderText(s))