from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



def init():
    path = 'C://Users//yossi//Desktop//Python-Project//ATID_Website_Automation_Testing//Driver//chromedriver.exe'
    driver = webdriver.Chrome(path)
    url = 'https://atid.store/'
    driver.get(url)
    driver.maximize_window()
    sleep(5)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Contact").click()
    return driver

init()