from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://sauce-demo.myshopify.com/")

# shows list of available colors of an item
# works for only one item

# goes to product page
product_link = driver.find_element(By.CSS_SELECTOR, "a[href*='/products/noir-jacket']")
product_link.click()

time.sleep(2)

# finds the color dropdown
dropdowns = driver.find_elements(By.CSS_SELECTOR, "select.single-option-selector[data-option='option2']")
assert len(dropdowns) > 0, "No dropdowns found for the catalog item."
select = Select(dropdowns[0])
available_colors = [option.text.strip() for option in select.options]

# output in cmd
print("Item has different colors. Available colors: ", available_colors)

driver.quit()