from behave import *
from selenium.webdriver.common.by import By

@given('Open target app main page')
def open_mainpage(context):
    context.driver.get('https://www.target.com/')

@when('Clicked on Sign In')
def click_on_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()
    context.driver.find_element(By.XPATH, "//button[@type='button' and text()='Sign in or create account']").click()

@then('Verify Sign In form is opened')
def verify_sign_in(context):
    expected_text3 = 'Sign in or create account'
    actual_text3 = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    assert expected_text3 in actual_text3, f'Error: expected "{expected_text3}", not found in "{actual_text3}"'