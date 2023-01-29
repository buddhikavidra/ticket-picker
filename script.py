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
#time duration amaog 
customiterval = 1

evetame = config.get('DEFAULT','evetame')
PageNumber = config.get('DEFAULT','pageNo')
EventNoInPageFromTop=config.get('DEFAULT','EventNoInPageFromTop')


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


def PageSelection_EventSelectioPage():

    #GettextPage = driver.find_element('xpath' , "(//td/span[contains(@id,'PageInfo')])[1]").text
    #a=GettextPage.split
    a1= int(PageNumber)

    if a1==1:
        print("Page Number : " + PageNumber)
    else :
        for iter in range(1 , a1):
            converted_num = str(iter+1)   
            print("Page Number : " + converted_num)
            driver.find_element('xpath', "(//input[contains(@id,'btnNextPage')])[1]").click() 
            time.sleep(2)


def error_Message():
    driver.find_element('xpath', "//a[text()='Back']").click()

def login():
    driver.get("https://tickets.fcbayern.com/internetverkaufzweitmarkt/EventList.aspx")
    time.sleep(5)
    try:
        driver.find_element('xpath', "//span[text()='Login']").click()
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
    except:
        print("already logged in or error in the login")
    time.sleep(5)
    PageSelection_EventSelectioPage()
    try:
        driver.find_element('xpath', "(//img[contains(@id,'EventImage')])["+EventNoInPageFromTop+"]/ancestor::div[@class='side-box-container']/descendant::a[text()='buy online']").click()
        time.sleep(7)
        #driver.find_element('xpath', "//span[text()='Ticket selection']").click()
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.save_screenshot("Tickets Available"+generate_random_string(5)+".png")
    except:
        print("event click failed")
        driver.save_screenshot("eventclickfailed"+generate_random_string(5)+".png")
        

login()

"""
try:
        driver.find_element('xpath', '//span[@class="icon icon-user button-icon is-white type-icon"]')
except:
        login()
GetCount = driver.find_elements('xpath', "//a[contains(text(),'Add to')]")   
count = len(GetCount)
print("Available Ticket Count : " +count)
c1 =  int(count) 
for iter in range(1 , c1+1):
   try: 
        if c1==1:
            driver.find_element('xpath', "(//a[contains(text(),'Add to')])[1]").click()
        else:
            driver.find_element('xpath', "(//a[contains(text(),'Add to')])[1]").click()
   except:       
        driver.refresh()
        tme = random.randint(1, 50)
        print("wait time : "+str(tme))
        time.sleep(tme)   

"""          
time.sleep(5)
a = 1
while True:
    print("itr : "+ str(a))
    try:
        driver.find_element('xpath', '//span[@class="icon icon-user button-icon is-white type-icon"]')
    except:
        login()
    try:
        GetCount = driver.find_elements('xpath', "//a[contains(text(),'Add to')]")   
        count = len(GetCount)
        print("Available Ticket Count : " +count)
        c1 =  int(count) 
        driver.find_element('xpath', "(//a[contains(text(),'Add to')])[1]").click()
        #driver.save_screenshot("sucess"+generate_random_string(5)+".png")
        time.sleep(1)
        VisibilityElementErrorMsg = driver.find_element('xpath' , "//h1[@itemprop='headline']/span[contains(@id,'ErrorMessages1')]")

        if VisibilityElementErrorMsg.is_displayed:
            print("Error Message is displayed") 
            error_Message()
        else :
           print("Error Message is Not displayed")

    except:
        print("No tickets found || Start refreshing")
        driver.refresh()
        tme = random.randint(1, 50)
        print("wait time : "+str(tme))
        time.sleep(tme)
    a=a+1


