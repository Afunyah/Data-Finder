from subprocess import Popen
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class Crawler():
    
    chromeBots = {
        "linkedin" : {
            "driver" : None,
            "port" : "9222",
            "proc" : None
            },
        "search" : {
            "driver" : None,
            "port" : "9223",
            "proc" : None
            },
    }

    def __init__(self):        
        for k,v in self.chromeBots.items():
            chrome_command = [
                "Google Chrome",
                "--args",
                f"--remote-debugging-port={v['port']}",
                "--user-data-dir=" + f"xChromeProfile_{k}",
            ]
            proc = Popen(chrome_command, stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
            
            chrome_options = Options()
            chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{v['port']}")
            
            v["driver"] = webdriver.Chrome(options=chrome_options)
            v["proc"] = proc
            
    def initiateDriverSetup(self):
        self.chromeBots["linkedin"]["driver"].get("https://www.linkedin.com/login")
        self.chromeBots["search"]["driver"].get("https://www.google.com")
        
    def searchLinkedin(self, url):
        self.chromeBots["linkedin"]["driver"].get(url)        
        
    def searchCompany(self, company):
        company_parsed = company.replace(" ","+")
        search_url = f"https://www.google.com/search?q={company_parsed}"
        self.chromeBots["search"]["driver"].get(search_url)
        
    def getLinkedinPictureURL(self):
        pic_url = ""
        
        try:
            pic_elem = WebDriverWait(self.chromeBots["linkedin"]["driver"], 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.pv-top-card__photo>img'))
            )
            if "ghost-person" in pic_elem.get_attribute('class'):
                raise Exception("Ghost Picture")
            
            pic_url = pic_elem.get_attribute('src')
        except:
            print("Could Not Get Profile Picture")
        
        
        return pic_url
    
    def terminate(self):
        for k,v in self.chromeBots.items():
            try:
                v["driver"].close()
            except:
                pass
            try:
                v["proc"].kill()
            except:
                pass