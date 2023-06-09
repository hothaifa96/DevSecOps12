from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get('https://amazon.com')
driver.maximize_window()


input = WebDriverWait.until(10,units=EC.)
driver.find_element(By.CSS_SELECTOR,'#twotabsearchtextbox')
input.send_keys('iphone 11 pro max cases')
input.send_keys(Keys.ENTER)

time.sleep(10)