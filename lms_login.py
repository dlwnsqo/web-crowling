from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip

id = 'uyiuy97'
pw = 'wnsqo218@'

driver = webdriver.Chrome('C:\\Users\\Boat\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get('https://lms.knu.ac.kr/ilos/main/main_form.acl')
#driver.maximize_window()
#driver.find_element_by_name('//*[@id="header"]/div[4]/ul/a/li').click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[4]/ul/a/li'))).click()

pyperclip.copy(id)
driver.find_element_by_xpath('//*[@id="usr_id"]').send_keys(Keys.CONTROL, 'v')
pyperclip.copy(pw)
driver.find_element_by_xpath('//*[@id="usr_pwd"]').send_keys(Keys.CONTROL, 'v')
driver.find_element_by_xpath('//*[@id="login_btn"]').click()
#login

#driver.find_element_by_xpath('//*[@id="contentsIndex"]/div[2]/div[2]/ol/li[4]/em').click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contentsIndex"]/div[2]/div[2]/ol/li[4]/em'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="week-2"]/div'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lecture-2"]/div/ul/li[1]/ol/li[5]/div/div/div[1]/div/span'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="front-screen"]/div/div[2]/div[1]/div'))).click()
