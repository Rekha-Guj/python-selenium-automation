from behave import *
from selenium.webdriver.common.by import By
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[id='addToCartButtonOrTextIdFor12954617']")
Order_PICKUP_BTN = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
ADD_TO_CART_SIDE_BTN = (By.CSS_SELECTOR, "button[data-test='fulfillment-cell-pickup']")
CART_ICON = (By.CSS_SELECTOR, "a[class*='styles_ndsBaseButton__W8Gl7 styles_md__X_r95']")
ADDED_PRODUCT_NAME = (By.XPATH, "//div[text()='Tazo Organic Tea Latte Chai Black Tea - 32 fl oz']")
# product_name = "[data-test='cartItem-title']"
IN_CART_PRODUCT_NAME = (By.XPATH, "//div[text() = 'Tazo Organic Tea Latte Chai Black Tea - 32 fl oz']")
PRODUCT_COLORS = (By.CSS_SELECTOR, "a[aria-label*='Color']")

@step('Click on Add to Cart button')
def click_on_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.find_element(*Order_PICKUP_BTN).click()
    context.driver.find_element(*ADD_TO_CART_SIDE_BTN).click()
    sleep(1)

@step('Click on Shopping cart icon')
def click_on_shopping_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(5)

@then('Verify that the added product is available in the Cart')
def verify_added_product(context):

    context.added_product_name = context.driver.find_element(*ADDED_PRODUCT_NAME).text
    context.product_name_in_cart = context.driver.find_element(*IN_CART_PRODUCT_NAME).text
    sleep(5)
    print(f'Added product name: {context.added_product_name}')
    print(f'In-Cart Product name: {context.product_name_in_cart}')

    # assert actual_product_name == product_name_in_cart, "f: Error, product is not available in the cart "

    assert context.added_product_name[:9] == context.product_name_in_cart[:9], \
        "f: Error, product is not available in the cart "


@given('Open target product page')
def target_prod_page(context):
    (context.driver.get
     (f'https://www.target.com/p/women-s-high-rise-utility-barrel-jeans-universal-thread/-/A-93533635?preselect=93390852#lnk=sametab'))
    sleep(9)

@then('Verify user can click through colors')
def verify_prod_colors(context):
    expected_colors = ['Olive Green', 'Black', 'Medium Wash', 'Pink']
    actual_colors = []

    colors = context.driver.find_elements(*PRODUCT_COLORS)
    for color in colors:
        color.click()













