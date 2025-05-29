from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

# Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo")

# Email field
driver.find_element(By.ID,'ap_email_login')

# Continue button
driver.find_element(By.XPATH, "//input[@class='a-button-input']")

# Conditions of use link
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")

# Privacy Notice link
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")

# Need help link
driver.find_element(By.XPATH, "//a[@class='a-size-base a-link-normal']")

# Forgot your password link
driver.find_element(By.XPATH,"//a[@id='auth-fpp-link-bottom']")

# Other issues with the Sign-In link
driver.find_element(By.XPATH,"//a[@id='ap-other-signin-issues-link']")

# Create your Amazon account button
driver.find_element(By.XPATH,"//a[@id='createAccountSubmit']")
