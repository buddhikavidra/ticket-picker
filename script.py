import undetected_chromedriver.v2 as uc
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import csv
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import configparser
import os



config = configparser.ConfigParser()
config.read('config.ini')
userame = config.get('DEFAULT','userame')
eventurl = config.get('DEFAULT','event')
current_directory = os.getcwd()
#time duratio amaog 
customiterval = 1

evetame = 'FC Bayern München -  Eintracht Frankfurt'



options = uc.ChromeOptions()

# setting profile
options.user_data_dir = str(current_directory)+"/"+userame

driver = uc.Chrome(executable_path=ChromeDriverManager().install(),options=options)

driver.get("https://tickets.fcbayern.com/internetverkaufzweitmarkt/EventList.aspx")

asd = input("if you didt login 1st time maually login after that you dot eed to login uless you chage the directory")

time.sleep(5)

driver.find_element('xpath', "//span[text()='"+evetame+"']/ancestor::div[@class='side-box-container']/descendant::a[text()='buy online']").click()

#//span[@class="select2-results"]/ul/li[contains(text(),'Kategorie 4')]
#//span[text()='FC Bayern München -  Eintracht Frankfurt']/ancestor::div[@class='side-box-container']/descendant::a[text()='buy online']
#driver.save_screenshot("full_page_screenshot.png")
