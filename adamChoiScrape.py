from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = webdriver.ChromeService(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

input_element = driver.find_element(By.CLASS_NAME, "RNNXgb")
input_element.send_keys("tech with tim" + Keys.ENTER)

time.sleep(120)

driver.quit()