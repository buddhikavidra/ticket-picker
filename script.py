import undetected_chromedriver.v2 as uc
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains
import configparser
import os
import random
import string


config = configparser.ConfigParser()
config.read('config.ini')
userame = config.get('DEFAULT','userame')
eventurl = config.get('DEFAULT','event')
current_directory = os.getcwd()
#time duratio amaog 
customiterval = 1

evetame = 'FC Bayern München - 1. FC Union Berlin'



options = uc.ChromeOptions()

# setting profile
options.user_data_dir = str(current_directory)+"/"+userame

driver = uc.Chrome(executable_path=ChromeDriverManager().install(),options=options)

driver.get("https://tickets.fcbayern.com/internetverkaufzweitmarkt/EventList.aspx")
driver.maximize_window()

#asd = input("if you didt login 1st time maually login after that you dot eed to login uless you chage the directory")

time.sleep(5)
def generate_random_string(string_length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(string_length))

driver.find_element('xpath', "//span[text()='Login']").click()
time.sleep(5)
def login():
    username = "gerhardtbeats2@outlook.com"
    password = "Newpassword1102!"
    time.sleep(2)
    driver.find_element('xpath', '//input[@id="username"]').click()
    driver.find_element('xpath', '//input[@id="username"]').clear()
    driver.find_element('xpath', '//input[@id="username"]').send_keys(username)
    
    time.sleep(1)
    driver.find_element('xpath', '//input[@id="password"]').click()
    driver.find_element('xpath', '//input[@id="password"]').clear()
    driver.find_element('xpath', '//input[@id="password"]').send_keys(password)
    time.sleep(1)
    driver.find_element('xpath', '//button[@name="login"]').click()
    time.sleep(5)
    try:
        driver.find_element('xpath', "//span[text()='"+evetame+"']/ancestor::div[@class='side-box-container']/descendant::a[text()='buy online']").click()
        time.sleep(7)
        driver.find_element('xpath', "//span[text()='Ticket selection']").click()
    except:
        print("event click failed")
        driver.save_screenshot(generate_random_string(5)+".png")
#//span[@class="select2-results"]/ul/li[contains(text(),'Kategorie 4')]
#//span[text()='FC Bayern München -  Eintracht Frankfurt']/ancestor::div[@class='side-box-container']/descendant::a[text()='buy online']
#driver.save_screenshot("full_page_screenshot.png")
#//a[contains(text(),'Add to')]
login()
#driver.get("https://tickets.fcbayern.com/internetverkaufzweitmarkt/SelectTicketMarketTickets.aspx")
time.sleep(5)
a = 1
while True:
    print("itr : "+ str(a))
    try:
        driver.find_element('xpath', '//span[@class="icon icon-user button-icon is-white type-icon"]')
    except:
        login()
    try:
        driver.find_element('xpath', "//a[contains(text(),'Add to')]")
        driver.save_screenshot(generate_random_string(5)+".png")
    except:
        print("ot fou tickets refreshig")
        driver.refresh()
        time.sleep(5)
    a=a+1