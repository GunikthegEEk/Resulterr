import time
import unittest
from PIL import Image
from selenium import webdriver
from Screenshot import Screenshot_Clipping
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions() 
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
options.add_argument(r"user-data-dir=C:\Users\GunikthegEEk\AppData\Local\Google\Chrome\AUPro") #Path to your chrome profile
options.add_argument("--headless")  
driver = webdriver.Chrome(executable_path=r"C:\Users\GunikthegEEk\Documents\Resuterr\chromedriver.exe", chrome_options=options)
#options.addArguments("--no-sandbox")
driver.set_page_load_timeout(15)

def get_result(curr_roll):
    try:
        driver.get("https://mis.nitrr.ac.in/publishedresult.aspx")
        roll =driver.find_element_by_id("txtRegno")
        roll.send_keys(curr_roll)
        roll.send_keys(Keys.ENTER)
        time.sleep(2)
        nameel = driver.find_element_by_xpath('//*[@id="lblSName"]')
        name = nameel.text
        sem = driver.find_element_by_xpath('//*[@id="ddlSemester"]/option[2]')
        sem.click()
        #time.sleep(5)
        show = driver.find_element_by_id('btnimgShowResult')
        show.click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        s= driver.find_element_by_xpath('//*[@id="form1"]/table[2]/tbody/tr[1]/td')
        ob=Screenshot_Clipping.Screenshot()
        img_url=ob.get_element(driver, s, r'.')
        print(img_url)
        #driver.quit()
    except:
        NoSuchElementException

for rolls in range(19223079,19223094):
    get_result(rolls)