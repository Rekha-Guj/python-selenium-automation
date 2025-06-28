from behave import *
from selenium.webdriver.common.by import By
from time import sleep

# HW_3

SHOPPING_CART_IS_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

@then('Verify that the shopping cart is empty')
def step_impl(context):
    # expected_text2 = 'Your cart is empty'
    # actual_text2 = context.driver.find_element(*SHOPPING_CART_IS_EMPTY_MSG).text
    # assert expected_text2 in actual_text2, f'error, expected {expected_text2}, not in {actual_text2}'
    # sleep(1)
    # print("Test Passed")

    context.app.header.verify_empty_shopping_cart()