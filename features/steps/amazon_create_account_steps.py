from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open Amazon account creation page')
def amazon_account(context):
    context.driver.get('https://www.amazon.com/gp/css/homepage.html?ref_=nav_AccountFlyout_ya')
    sleep(1)
    # context.driver.find_element(By.XPATH, "//span[contains(text(), 'Browse self service options, help articles or contact us')]")
    # context.driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/hz/contact-us?ref_=nav_AccountFlyout_CS']").click()
    context.driver.find_element(By.XPATH, "//a[text()='Customer Service']").click()
    sleep(1)
    context.driver.find_element(By.XPATH, "//div[@class='center fs-match-card-detail']//div[text()='Something else']").click()
    sleep(2)

@when('User details are entered')
def user_details(context):
    context.driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit").click()
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#ap_customer_name").send_keys("Re")
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#ap_email").send_keys("rguj@gmail.com")
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#ap_password").send_keys("NeeOm@999")
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#ap_password_check").send_keys("NeeOm@999")
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "#continue").click()
    sleep(1)

@then('Verify account is created and user is logged to Amazon app')
def verify_account_is_created(context):
    expected_text1 = 'Verify email address'
    actual_text1 = context.driver.find_element(By.XPATH, "//h1[text()='Verify email address']").text
    sleep(2)
    assert expected_text1 in actual_text1, f"error, expected {expected_text1}, not available in {actual_text1}"
    print("Test is Passed")