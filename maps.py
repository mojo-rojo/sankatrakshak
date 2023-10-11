from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
username = "thane"
# password = input('give password')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://maps-generator.com/")
uname = driver.find_element("id", "street") 
uname.send_keys("thane")
driver.find_element("id", "get_code_btn").click()
time.sleep(4)
driver.find_element(By.CLASS_NAME, "btn btn-success code-copy").click()
