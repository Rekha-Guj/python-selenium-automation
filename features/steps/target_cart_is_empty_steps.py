from behave import *
from selenium.webdriver.common.by import By
from time import sleep

# HW_3


@then('Verify that the shopping cart is empty')
def step_impl(context):
    expected_text2 = 'Your cart is empty'
   # actual_text2 = context.driver.find_element(By.XPATH, "//h1[@class='styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh']").text
    actual_text2 = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_text2 in actual_text2, f'error, expected {expected_text2}, not in {actual_text2}'
    sleep(1)
    print("Test Passed")