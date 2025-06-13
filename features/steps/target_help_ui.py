from behave import *
from selenium.webdriver.common.by import By
from time import sleep

# HW_4

@given('Open target help page')
def open_target_help_page(context):
    context.driver.get("https://help.target.com/help")
    sleep(1)

@then('Verify the elements present on Help page')
def verify_elements_present(context):
    title = context.driver.find_element(By.XPATH, "//h2[@class='custom-h2']").text
    context.driver.find_element(By.XPATH, "//input[@id='j_id0:j_id2:j_id44:name']")
    context.driver.find_element(By.XPATH, "//input[@class='btn-sm search-btn']")
    context.driver.find_element(By.XPATH, "//div[@class='col-lg-12']")
    context.driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']")

