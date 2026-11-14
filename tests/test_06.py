import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_buy_3_items():
    driver = webdriver.Chrome()
    driver.get("https://sauce-demo.myshopify.com/collections/frontpage/products/grey-jacket")
    driver.find_element(By.ID, "add").click() #clicks add to cart

    time.sleep(2)  

    driver.get("https://sauce-demo.myshopify.com/cart") #get cart

    time.sleep(2)
    boxes = driver.find_elements(By.NAME, "updates[]") #gets all qty boxes
    qty = [b for b in boxes if b.is_displayed()][0] #picks first visible box

    qty.clear()
    qty.send_keys("3") #types 3 in box
    qty.send_keys(Keys.RETURN) #presses enter to submit and update cart

    time.sleep(2)

    driver.get("https://sauce-demo.myshopify.com/cart") #verification test 
    time.sleep(2)
    boxes = driver.find_elements(By.NAME, "updates[]")
    qty = [b for b in boxes if b.is_displayed()][0]
    assert qty.get_attribute("value") == "3"

    driver.quit()

test_buy_3_items()
