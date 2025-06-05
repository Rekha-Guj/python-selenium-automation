from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

# Open application link
driver.get("https://www.target.com/")

driver.find_element(By.XPATH, "//span[@class='sc-43f80224-3 fBDEOp h-margin-r-x3']").click()
print("Account")
sleep(2)
driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in or create account')]").click()
sleep(2)
# Verify SignIn page opened
expected_text = "Sign in or create account"
actual_text = driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text

assert expected_text in actual_text, f"error, expected {expected_text}, not in {actual_text}"
print(f"{actual_text} is present")

driver.find_element(By.XPATH, "//button[@class='styles_ndsBaseButton__W8Gl7 styles_lg___H2IL styles_lgGap__bPB7P styles_fullWidth__3XX6f styles_ndsButton__XOOOH styles_lg__T5sAi styles_filleddefault__7QnWt']").click()
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("rgujalwar@gmail.com")
sleep(2)
#driver.find_element(By.XPATH, "//form//button[@id='login' and @type='submit' and contains(text(), 'Continue')]").click()

driver.find_element(By.XPATH, "//button[@id='login']").click()


driver.get("https://www.target.com/")
driver.find_element(By.XPATH,"//input[@id='search']").send_keys("chocolates")
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(2)
expected_text = "chocolates"
actual_text = driver.find_element(By.XPATH, "//span[contains(text(),'for')]").text

# Verification
assert expected_text in actual_text, f"error, expected {expected_text}, not in {actual_text}"
print("Test is Passed")


# driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys("rekha")
# driver.find_element(By.XPATH, "//input[@id='lastname']").send_keys("gujal")
# driver.find_element(By.XPATH, "//input[@name='phonecreateAccount']").send_keys("2018844426")
# driver.find_element(By.XPATH, "//label[@class='styles_ndsLabel__By3p6' and @for='password-checkbox']").click()
# driver.find_element(By.XPATH, "//button[@id='createAccount']").click()
# driver.find_element(By.XPATH, "//input[@id='password']").send_keys("target@123")
# driver.find_element(By.XPATH, "//button[@id='createAccount']").click()
#
# driver.find_element(By.XPATH, "//input[@id='search']").send_keys("chocolates")
# driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#
# # verification
# expected_text = "chocolates"
# actual_text = driver.find_element(By.XPATH, "//span[contains(text(),'for “chocolates”')]").text
#
# assert expected_text in actual_text, f"error, expected {expected_text}, not in {actual_text}"
# print("Test Case Passed")
#
driver.close()
driver.quit()