import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

BASE = "https://sauce-demo.myshopify.com"
PRODUCT_URL = f"{BASE}/products/flower-print-jeans"   

# Shopify themes use either a <select> dropdown or radio buttons for options.
SIZE_SELECT = "select[id*='Option'], select[name*='ize'], select[name='id']"
SIZE_RADIOS = "fieldset input[type='radio'], .swatch input[type='radio']"
ADD_TO_CART = "button[name='add'], form[action*='/cart/add'] [type='submit']"


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()


def pick_non_default_size(driver):
    """Selects a size other than the default one. Returns the chosen size text."""
    size_el = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Size']/following::select[1]")
        )
    )
    dropdown = Select(size_el)
    default = dropdown.first_selected_option.text.strip()

    for opt in dropdown.options:
        text = opt.text.strip()
        if text and text != default and opt.is_enabled():
            dropdown.select_by_visible_text(text)
            assert dropdown.first_selected_option.text.strip() == text
            return text

    pytest.fail(f"Size dropdown only has the default option: {default}")

def test_item_with_non_default_size(driver):
    driver.get(PRODUCT_URL)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ADD_TO_CART)))

    chosen_size = pick_non_default_size(driver)
    print(f"\nChosen non-default size: {chosen_size}")

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ADD_TO_CART))).click()
    time.sleep(2)  # let the AJAX add finish (replace with a proper wait if you can)

    driver.get(f"{BASE}/cart")
    wait.until(EC.url_contains("/cart"))
    cart_text = driver.find_element(By.TAG_NAME, "body").text

    # The cart line should show the size we picked (e.g. "Size: M")
    assert chosen_size in cart_text, f"Size '{chosen_size}' not found in cart"