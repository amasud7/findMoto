from selenium import webdriver
from selenium.webdriver.common.by import By

# adding headless option for firefox
# head = webdriver.FirefoxOptions()
# head.add_argument("--headless")

driver = webdriver.Firefox() # which browser it opens
driver.implicitly_wait(1) # wait for elements to load in page
driver.get("https://www.facebook.com/marketplace/dallas/search/?query=motorcycle&exact=false")


# now to close the x
driver.find_element(By.XPATH, '').click()