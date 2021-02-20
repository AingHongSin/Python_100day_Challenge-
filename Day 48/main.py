from selenium import webdriver

chrome_driver_path = "/Users/ainghongsin/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

# price = driver.find_element_by_class_name("p13n-sc-price")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="container"]/li[4]/ul/li[5]/a')
# print(bug_link.text)

# dist = driver.find_element_by_class_name("menu")
# print())


event_time = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

event = {}

for n in range(len(event_time)):

    event[n] = {
        "time": event_time[n].text,
        "name": event_names[n].text,
    }

print(event)





driver.close()
driver.quit()