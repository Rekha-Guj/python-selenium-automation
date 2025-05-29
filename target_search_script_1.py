from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Driver instances
driver = webdriver.Chrome()
driver.maximize_window()

# open url
driver.get("https://www.target.com/")
driver.find_element(By.ID, "search").send_keys('tea')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)
print("got the search")

# Verification / Assertion
expected_text = 'tea'
actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text

# Other way
# if expected_text in actual_text:
#     print("The Test has Passed")
# else:
#     print("The Test has Failed.")

assert expected_text in actual_text, f"Error, Expected: {expected_text} not in Actual: {actual_text}"

print("Test case is Passed")

sleep(10)

driver.close()
driver.quit()