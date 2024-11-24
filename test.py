from subprocess import Popen

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chromeBots = {
    "linkedin" : {
        "driver" : None,
        "port" : "9222"
        },
    "search" : {
        "driver" : None,
        "port" : "9223"
        },
}

for k,v in chromeBots.items():
    print(k)
    chrome_command = [
        "Google Chrome",
        "--args",
        f"--remote-debugging-port={v['port']}",
        "--user-data-dir=" + f"xChromeProfile_{k}",
    ]
    Popen(chrome_command)
    
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{v['port']}")
    
    v["driver"] = webdriver.Chrome(options=chrome_options)

chromeBots["linkedin"]["driver"].get("https://www.next.co.uk")
chromeBots["search"]["driver"].get("https://www.jaguar.co.uk")