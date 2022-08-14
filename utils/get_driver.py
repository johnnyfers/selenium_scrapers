import os
from selenium import webdriver

def get_driver():
    driver_path = os.path.abspath('drivers/chromedriver_linux64/chromedriver')
    driver = webdriver.Chrome(driver_path)
    
    return driver
