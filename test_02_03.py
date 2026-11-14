from selenium import webdriver                                   # opening the browser
from selenium.webdriver.common.by import By                      # By.ID, By.NAME, etc.
from selenium.webdriver.common.keys import Keys                  # Keys.ENTER, Keys.TAB, etc.
from selenium.webdriver.support.ui import WebDriverWait          # waiting for things
from selenium.webdriver.support import expected_conditions as EC # what to wait for
from selenium.webdriver.support.ui import Select                 # dropdowns
from selenium.webdriver.common.action_chains import ActionChains # hover, drag, right-click
import time                                                      # time.sleep()

driver = webdriver.Chrome()

driver.get("https://sauce-demo.myshopify.com")

#======== LOGIN ========

# click login button
el = driver.find_element(By.ID, "customer_login_link")
time.sleep(5)
el.click()
time.sleep(5)
# input email address
el = driver.find_element(By.ID, "customer_email")
el.click()
el.send_keys("baddielola@gmail.com")
time.sleep(3)
# input password
el = driver.find_element(By.ID, "customer_password")
el.click()
el.send_keys("mamacoco123")
time.sleep(3)
# click button
el = driver.find_element(By.CSS_SELECTOR, "input[value='Sign In']")
el.click()
time.sleep(5)


input("If there's CAPTCHA in Chrome then solve, then press Enter here...")

#======== ADD 3 ITEMS TO CART ========

el = driver.find_element(By.CSS_SELECTOR, "a[href='javascript:history.back()']")
if el:
    el.click()
    time.sleep(5)

el = driver.find_element(By.CSS_SELECTOR, "a[href='/collections/all']")
el.click()
time.sleep(5)

el = driver.find_element(By.CSS_SELECTOR, "img[src='//sauce-demo.myshopify.com/cdn/shop/products/shoes3_large.jpg?v=1394656926']")
el.click()
time.sleep(5)

el = driver.find_element(By.CSS_SELECTOR, "[value='Add to Cart']")
el.click()
time.sleep(5)

el = driver.find_element(By.CSS_SELECTOR, "a[href='/collections/all']")
el.click()
time.sleep(5)


el = driver.find_element(By.CSS_SELECTOR, "img[src='//sauce-demo.myshopify.com/cdn/shop/products/shoes_large.jpg?v=1394656541']")
el.click()
time.sleep(5)

el = driver.find_element(By.CSS_SELECTOR, "[value='Add to Cart']")
el.click()
time.sleep(5)

el = driver.find_element(By.CSS_SELECTOR, "a[href='/collections/all']")
el.click()
time.sleep(5)

el = driver.find_element(By.CSS_SELECTOR, "img[src='//sauce-demo.myshopify.com/cdn/shop/products/fleece_large.jpg?v=1394656989']")
el.click()
time.sleep(5)

el = driver.find_element(By.CSS_SELECTOR, "[value='Add to Cart']")
el.click()
time.sleep(5)

input("Press enter to close the browser...")
driver.quit()