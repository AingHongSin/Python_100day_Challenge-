from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/ainghongsin/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

fName = driver.find_element_by_name("fName")
fName.send_keys("AING")

lName = driver.find_element_by_name("lName")
lName.send_keys("Hongsin")

email = driver.find_element_by_name("email")
email.send_keys("Ainghongsin@gmail.com")
email.send_keys(Keys.ENTER)

click = driver.find_element_by_css_selector(" .btn-primary")
click.click()