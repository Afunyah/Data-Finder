import main
import time


startuptext ="""

███████╗██╗ ██████╗ ███╗   ███╗ █████╗ 
██╔════╝██║██╔════╝ ████╗ ████║██╔══██╗
███████╗██║██║  ███╗██╔████╔██║███████║
╚════██║██║██║   ██║██║╚██╔╝██║██╔══██║
███████║██║╚██████╔╝██║ ╚═╝ ██║██║  ██║
╚══════╝╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝

🚀 Information Finder Program v4.2.1 🚀
-------------------------------------
🌟 Enter 'start' after the prompt to run the program 💻
"""


print(startuptext)

main.crawler.initiateDriverSetup()

tostart = ""
while 'start' not in tostart.lower():
    tostart = input("Enter 'start' to start the program: ")
    continue

print("""
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------
""")

print("Application is running. Please interact with the main window which should have opened by now\n\n")

main.run()

print("Done")