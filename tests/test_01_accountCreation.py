from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get("https://sauce-demo.myshopify.com/account/register")
driver.implicitly_wait(10)

firstNameElement = driver.find_element(By.NAME, "customer[first_name]")
firstNameElement.click()
firstNameElement.send_keys("Mama")

lastNameElement = driver.find_element(By.NAME, "customer[last_name]")
lastNameElement.click()
lastNameElement.send_keys("Coco")

emailAddressElement = driver.find_element(By.NAME, "customer[email]")
emailAddressElement.click()
emailAddressElement.send_keys("baddielola@gmail.com")

passwordElement = driver.find_element(By.NAME, "customer[password]")
passwordElement.click()
passwordElement.send_keys("mamacoco123")

createElement = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Create']")
createElement.click()

time.sleep(30)
driver.quit()