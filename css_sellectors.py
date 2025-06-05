from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amezon.com")

# By ID
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox").click()

# By tag
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox").click()

# By class
driver.find_element(By.CSS_SELECTOR, ".nav-a")
driver.find_element(By.CSS_SELECTOR, ".nav-a.nav-a-2")
driver.find_element(By.CSS_SELECTOR, ".nav-a.nav-a-2.icp-link-style-2")

# By tag and class
driver.find_element(By.CSS_SELECTOR, "a.nav-logo-link.nav-progressive-attribute")

# By tag, ID and class
driver.find_element(By.CSS_SELECTOR, "a#nav-logo-sprites.nav-logo-link.nav-progressive-attribute")


# By Attribute
driver.find_element(By.CSS_SELECTOR, '[href="/ref=nav_logo"]')
driver.find_element(By.CSS_SELECTOR,'[aria-label="Amazon"]')

# By tag and Attribute
driver.find_element(By.CSS_SELECTOR, 'a[href="/ref=nav_logo"]')

# By multiple attributes
driver.find_element(By.CSS_SELECTOR,'[aria-label="Amazon"][lang="en"]')

# By class and multiple attributes
driver.find_element(By.CSS_SELECTOR,'.nav-logo-link[aria-label="Amazon"][lang="en"]')

# By ID, class, and multiple attributes
driver.find_element(By.CSS_SELECTOR,'#nav-logo-sprites.nav-logo-link[aria-label="Amazon"][lang="en"]')

# By tag, ID, class, and multiple attributes
driver.find_element(By.CSS_SELECTOR,'a#nav-logo-sprites.nav-logo-link[aria-label="Amazon"][lang="en"]')

# By using attribute partial search --> use *=
# Full --> [href="/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088"]
# Partail --> [href*="ap_signin_notification_condition_of_use"]
driver.find_element(By.CSS_SELECTOR, '[href*="ap_signin_notification_condition_of_use"]')
# Partial match using class
driver.find_element(By.CSS_SELECTOR, "[class*='styles_inputWrapper'][class*='styles_ndsTextField']")

































