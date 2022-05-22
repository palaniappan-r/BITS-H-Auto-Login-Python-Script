#A Python script that uses selenium to automate BITS Hyderabad's WiFIi login system

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

username = "" #add username here
password = "" #add password here

def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   driver.find_element(By.ID,usernameId).send_keys(username)
   driver.find_element(By.ID,passwordId).send_keys(password)
   driver.find_element(By.ID,submit_buttonId).click()

login("http://172.16.0.30:8090/","username",username,"password",password,"loginbutton")

driver.close()
