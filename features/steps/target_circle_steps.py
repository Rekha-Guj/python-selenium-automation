from selenium.webdriver.common.by import By
from behave import *
from time import sleep

# HW_4

@given('Open Target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')
    sleep(1)

@then('Verify there are at list 10 benefit cells')
def verify_target_circle_cells(context):
    cells_links = context.driver.find_elements(By.CSS_SELECTOR, "div[class*='sc-acea07d2-1'] a")
    sleep(1)
    print(len(cells_links))
    print(cells_links)

    assert len(cells_links) >= 10, f'Expected 10 cells, but found {len(cells_links)}'