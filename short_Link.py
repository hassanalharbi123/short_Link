print("""
\033[3;34m            █████████    ███      ███    ████████████    ██████████     ████████████   \033[3;31m     ██           ██   █████    ██    ██     ██
\033[3;34m            ██           ███      ███    ██        ██    ██      ██          ██        \033[3;31m     ██                ██  ██   ██    ██   ██
\033[3;34m            █████████    ████████████    ██        ██    ████████            ██        \033[3;31m     ██           ██   ██   ██  ██    ██████
\033[3;34m                   ██    ███      ███    ██        ██    ██      ██          ██        \033[3;31m     ██           ██   ██    ██ ██    ██    ██
\033[3;34m            █████████    ███      ███    ████████████    ██       ██         ██        \033[3;31m     █████████    ██   ██     ████    ██     ██
                                                        alhassan alharbi :\033[0;36m twitter ==>https://twitter.com/alhassanAlharb7\n""")
import os
os.system("pip install pyshorteners")
import pyshorteners
from webbrowser import open

url=input("\033[3;35menter the url \n")
a=pyshorteners.Shortener()
b=a.tinyurl.short(url)
print("\033[0;36mthe new link is: ")
print("   ",b)
q=input("do you want open in browser [\033[3;31my\033[3;36m/\033[3;31mn\033[3;36m]\n")
if q=="y"or q=="yes":
	open(b)
else:
	exit()
