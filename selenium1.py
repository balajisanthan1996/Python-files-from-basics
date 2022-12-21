from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(executable_path = r"D:\webdriver_for_automation\geckodriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
driver.find_element(By.NAME ,'q').send_keys("Siemens")
driver.implicitly_wait(2)
Keys.ENTER
