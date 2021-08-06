'''
Created on May 9, 2020

@author: Chandan
'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

url="https://safety-red5.kuvrr.com/?next=/observer/"

from selenium import webdriver

driver = webdriver.Chrome(executable_path= 'C:\\Users\\Chandan\\Git\\chromedriver.exe')

driver.get(url)
print("Please Login ")

element=driver.find_element_by_xpath("//input[@id='email'][@name='email']")
element.send_keys("lackorg@yopmail.com")

