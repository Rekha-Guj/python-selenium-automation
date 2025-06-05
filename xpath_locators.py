from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from sample_script import service

# get the path to ChromeDriver
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Locators
# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

# By XPATH
driver.find_element(By.XPATH, "//input[@role='searchbox']")

# By XPATH and should work with any tag
driver.find_element(By.XPATH, "//*[@role='searchbox']")

# By XPATH and combinations of multiple elements [to narrow down our search], Note - Don't use more than 3
driver.find_element(By.XPATH, "//a[@aria-label='Amazon' and @lang='en']")
driver.find_element(By.XPATH, "//input[@dir='auto' and @role='searchbox' and @placeholder='Search Amazon']")
# OR using *
driver.find_element(By.XPATH, "//*[@dir='auto' and @role='searchbox' and @placeholder='Search Amazon']")
# OR - Order doesn't matter
driver.find_element(By.XPATH, "//*[@dir='auto' and @placeholder='Search Amazon' and @role='searchbox']")


# text() function
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
# text() function with a combination for a precise search
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# Partial Match --> Contains() function for lengthy attribute values
driver.find_element(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.XPATH, "//a[contains(@href, 'ref_=nav_cs_bestsellers')]")

# Nested Tag, Contains(), Text() of Target website
# --->>>>  //div[@data-test='lp-resultsCount']//span[contains(text(), 'for')]

# Nested tags for precise search
driver.find_element(By.XPATH, "//div[@id='navbar']//a[text()='Best Sellers']")






