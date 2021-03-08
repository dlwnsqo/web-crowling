from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

ID = 'uyiuy97'
password = 'wnsqo970'

driver = webdriver.Chrome('C:\\Users\\Boat\\Downloads\\chromedriver_win32\\chromedriver.exe')

driver.get('https://www.naver.com')
driver.find_element_by_xpath('//*[@id="account"]/a').click()
pyperclip.copy(ID)
driver.find_element_by_xpath('//*[@id="id"]').send_keys(Keys.CONTROL, 'v')

pyperclip.copy(password)
driver.find_element_by_xpath('//*[@id="pw"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="log.login"]').click()