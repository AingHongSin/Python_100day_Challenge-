from selenium import webdriver
import time

chrome_driver_path = "/Users/ainghongsin/Documents/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

item = "buy*"

cookie_counter = driver.find_element_by_css_selector("#money")
item_scraping = driver.find_elements_by_css_selector("#store b")

timeout_to_stop = time.time() + 60 * 5
time_to_upgrade = time.time() + 5

cost_list = []
items_list = []

for item in item_scraping:
    items_list.append(f"buy{item.text.split('-')[0].strip()}")

print(items_list.remove('buy'))

while True:

    sec = 0
    if sec == 5 or time.time() >= timeout_to_stop:
        break
    sec -= 1

    clicker = driver.find_element_by_css_selector("#cookie")

    if time.time() >= time_to_upgrade:
        for n in range(len(items_list) - 1, 0, -1):
            item_cost = driver.find_element_by_css_selector(f"#{items_list[n]} b")
            if cookie_counter >= item_cost:
                clicker.find_element_by_css_selector(f"#{items_list[n]}")



    clicker.click()