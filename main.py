import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_upgrade():
    upgrade_types = ["Cursor", "Grandma", "Factory", "Mine", "Shipment", "Alchemy\ lab", "Portal", "Time\ machine"]
    upgrades = []
    prices = []

    for upgrade in upgrade_types:
        upgrade_type = driver.find_element(By.CSS_SELECTOR, value=f"#buy{upgrade}")
        price = driver.find_element(By.CSS_SELECTOR, value=f"#buy{upgrade} > b:nth-child(1)")
        upgrades.append(upgrade_type)
        prices.append(price.text.split(" - ")[1].replace(",", ""))

    return {upgrades[i]: prices[i] for i in range(len(upgrades))}


driver = webdriver.Firefox()
driver.get("http://orteil.dashnet.org/experiments/cookie/ ")

cookie = driver.find_element(By.ID, value="cookie")
timeout = time.time() + 1

while True:
    cookie.click()

    if time.time() > timeout:
        ups = get_upgrade()
        cookie_count = driver.find_element(By.ID, value="money").text.replace(",", "")
        for up, price in reversed(ups.items()):
            if int(cookie_count) > int(price):
                up.click()
                break

        timeout = time.time() + 1

# driver.close() # Closes single tab
# driver.quit() # Shutdown entire browser
