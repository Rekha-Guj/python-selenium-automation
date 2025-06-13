from behave import *
from selenium.webdriver.common.by import By
from time import sleep

@then('Click on Add to Cart button')
def click_on_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[id='addToCartButtonOrTextIdFor12954617']").click()
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='fulfillment-cell-pickup']").click()
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='orderPickupButton']").click()
    sleep(1)

@then('Click on Shopping cart icon')
def click_on_shopping_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[class*='styles_ndsBaseButton__W8Gl7 styles_md__X_r95']").click()
    sleep(1)


@then('Verify that the added product is available in the Cart')
def verify_added_product(context):
    actual_product_name = context.driver.find_element(By.XPATH,
                                                      "//div[text()='Tazo Organic Tea Latte Chai Black Tea - 32 fl oz']").text
    expected_product_name = (
        context.driver.find_element(By.XPATH, "//div[text() = 'Tazo Organic Tea Latte Chai Black Tea - 32 fl oz']").text)
    assert actual_product_name == expected_product_name, "f:Error, product is not available in the cart "