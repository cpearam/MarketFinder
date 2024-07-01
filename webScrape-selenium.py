from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https:/lazada.com.ph")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "q"))
)

search_bar = driver.find_element(By.ID, "q")
search_bar.send_keys("yoyo" + Keys.ENTER)
time.sleep(10)