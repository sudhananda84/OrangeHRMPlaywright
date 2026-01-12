import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
backToTop=driver.find_element(By.XPATH,"//*[@id='navBackToTop']")
driver.execute_script("arguments[0].scrollIntoView('true')",backToTop)
socialmedialinks = driver.find_elements(By.XPATH, "//*[@id='navFooter']//following-sibling::div[@role='presentation']//*[contains(text(),'Amazon')]")

for link in socialmedialinks:
    driver.execute_script("arguments[0].style.border='3px solid red'",link)
    time.sleep(3)

driver.close()


