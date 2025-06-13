from behave import *
from selenium.webdriver.common.by import By
from time import sleep

@when('Clicked on Shopping cart icon')
def shopping_cart(context):
    #context.driver.find_element(By.XPATH, "//a[@aria-label='cart 0 items']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(2)

# @then('Verify header has correct amount of links')
# def header_links(context):
#     links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
#     print(len(links))
#     print(links)
#     assert len(links) == 6, 'Expected 6 links but got {len(links)}'

@then('Verify header has {number} links')
def verify_header_links(context, number):
    print(type(number))
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print(links)
    assert len(links) == int(number), f'Expected {number} links, but got {len(links)}'
