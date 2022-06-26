#%%
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd


class rva_calls():

    def __init__(self) -> None:
            
        # self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")

        self.url = "https://apps.richmondgov.com/applications/activecalls/"

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # self.driver = webdriver.Chrome(options=self.chrome_options, service=Service(ChromeDriverManager().install()))

    def __repr__(self) -> str:
        #TODO Name better
        return 'RVA Active Calls OBJ'
        
    def calls(self):
           
        self.driver.get(self.url)
        
        time.sleep(2)

        self.elem = self.driver.find_element(By.CLASS_NAME, "buttons-copy")

        self.elem.click()
        
        time.sleep(1)

        return pd.read_clipboard()
        
    def quit(self):
        
        self.driver.quit()

        print('Browser exited')

# %%
