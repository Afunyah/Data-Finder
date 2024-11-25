import main
import re


startuptext ="""

███████╗██╗ ██████╗ ███╗   ███╗ █████╗ 
██╔════╝██║██╔════╝ ████╗ ████║██╔══██╗
███████╗██║██║  ███╗██╔████╔██║███████║
╚════██║██║██║   ██║██║╚██╔╝██║██╔══██║
███████║██║╚██████╔╝██║ ╚═╝ ██║██║  ██║
╚══════╝╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝

🚀 Information Finder Program v4.2.1 🚀
-------------------------------------

Please take a moment to log in to your linkedin account (if you haven't already)
Please also decide which BATCH you are working on
🌟 Enter 'start' after the prompt to run the program 💻
"""


print(startuptext)

main.crawler.initiateDriverSetup()

tostart = ""
while 'start' not in tostart.lower():
    tostart = input("Enter 'start' to start the program: ")

batches = [
    "1-50", "51-100", "101-150", "151-200", "201-250", "251-300", "301-350", "351-400", 
    "401-450", "451-500", "501-550", "551-600", "601-650", "651-700", "701-750", "751-800", 
    "801-850", "851-900", "901-950", "951-1000", "1001-1050", "1051-1100", "1101-1150", 
    "1151-1200", "1201-1250", "1251-1300", "1301-1350", "1351-1400", "1401-1450", 
    "1451-1500", "1501-1550", "1551-1600", "1601-1650", "1651-1700", "1701-1716"
]

print("\nAvailable Batches:")
print(batches)
batch_num = ""
while batch_num not in batches:
    batch_num = input("\nPlease Enter a batch range (exact input required): ")

start_id = ""
while not start_id:
    start_id = input("\nPlease Enter a start ID within batch range: ")

print("""
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------
""")

print("Application is running. Please interact with the main window which should have opened by now\n\n")

batch_num = batch_num.replace("-","_")
batch_dir = f"data/batches/batch_{batch_num}"
input_file = f"{batch_dir}/original_{batch_num}.xlsx"
output_file = f"{batch_dir}/output_{batch_num}.xlsx"

main.initialize(input_file, output_file, start_id)
main.run()

print("Done")