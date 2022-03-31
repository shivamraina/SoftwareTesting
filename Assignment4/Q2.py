import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/srain/Downloads/chromedriver.exe')

# 1. Login functionality check
driver.get("https://mbasic.facebook.com")

email = driver.find_element_by_id("m_login_email") 
password = driver.find_element_by_name("pass")    

#  slowing down speed
for char in "rainshivam698@gmail.com":
    email.send_keys(char)
    time.sleep(0.3)

for char in 'Swagger@123':
    password.send_keys(char)
    time.sleep(0.3)

submit_button = driver.find_element_by_xpath("//input[@type ='submit']") 
submit_button.click()