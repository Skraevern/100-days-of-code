from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

search_input = driver.find_element(By.XPATH, value='//*[@id="searchInput"]')


search_input.send_keys("Python")
search_input.send_keys(Keys.ENTER)
search_input.send_keys(Keys.ENTER)
