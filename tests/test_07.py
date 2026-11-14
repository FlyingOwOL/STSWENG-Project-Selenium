from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

driver.get("https://sauce-demo.myshopify.com")

# Going to checkouts 
driver.find_element(By.ID, "product-1").click()
time.sleep(2)
driver.find_element(By.ID, "add").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "checkout").click()
driver.find_element(By.ID, "checkout").click()
time.sleep(5)

# Information input
instructions = driver.find_element(By.ID, "email")
instructions.click()
instructions.send_keys("baddielola@gmail.com")

instructions = driver.find_element(By.NAME, "lastName")
instructions.click()
instructions.send_keys("Coco")

instructions = driver.find_element(By.NAME, "address1")
instructions.click()
instructions.send_keys("Sa Puso Mo")

instructions = driver.find_element(By.NAME, "district")
instructions.click()
instructions.send_keys("Mexico")

instructions = driver.find_element(By.NAME, "postalCode")
instructions.click()
instructions.send_keys("9999")

instructions = driver.find_element(By.NAME, "city")
instructions.click()
instructions.send_keys("Saint Dennis")

time.sleep(2)

frame = driver.find_element(By.CSS_SELECTOR, "iframe[id^='card-fields-number']")
driver.switch_to.frame(frame)
instructions = driver.find_element(By.ID, "number")
instructions.click()
instructions.send_keys("1")
driver.switch_to.default_content()

frame = driver.find_element(By.CSS_SELECTOR, "iframe[id^='card-fields-expiry']")
driver.switch_to.frame(frame)
instructions = driver.find_element(By.ID, "expiry")
instructions.click()
instructions.send_keys("12")
instructions.send_keys("30")
driver.switch_to.default_content()

frame = driver.find_element(By.CSS_SELECTOR, "iframe[id^='card-fields-verification_value']")
driver.switch_to.frame(frame)
instructions = driver.find_element(By.NAME, "verification_value")
instructions.click()
instructions.send_keys("111")
driver.switch_to.default_content()

frame = driver.find_element(By.CSS_SELECTOR, "iframe[id^='card-fields-name']")
driver.switch_to.frame(frame)
instructions = driver.find_element(By.NAME, "name")
instructions.click()
instructions.send_keys("Test payment gateway")
driver.switch_to.default_content()

driver.find_element(By.ID,"checkout-pay-button").click()

time.sleep(5)

driver.quit()
