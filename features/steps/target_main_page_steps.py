from behave import *
from selenium.webdriver.common.by import By
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(1)