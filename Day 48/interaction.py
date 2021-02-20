from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "/Users/ainghongsin/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_counter = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')

# article_counter = driver.find_element_by_css_selector(" #articlecount a")
# print(article_counter.text)

# all_portales = driver.find_element_by_link_text("All portals")
# all_portales.click()

# search = driver.find_element_by_name('search')
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

fName_input = driver.find_element_by_name("fName")
fName_input.send_keys("AING")

lName_input = driver.find_element_by_name("lName")
lName_input.send_keys("Hongsin")

email_input = driver.find_element_by_name("email")
email_input.send_keys("ainghongsin@gmai.com")




# driver.close()
# driver.quit()