from selenium import webdriver
from selenium.webdriver.common.by import By


def upgrade():
    pass


driver = webdriver.Firefox()
driver.get("http://orteil.dashnet.org/experiments/cookie/ ")

cookie = driver.find_element(By.ID, value="cookie")

# while True:
#     cookie.click()


# driver.close() # Closes single tab
# driver.quit() # Shutdown entire browser
