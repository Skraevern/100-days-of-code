from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
)

price_dollar = driver.find_element(By.CLASS_NAME, value="a-offscreen")
print(price_dollar.text)

driver.get("https://www.python.org")
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)  # input
print(search_bar.get_attribute("placeholder"))  # Search

button = driver.find_element(By.ID, value="submit")
print(button.size)  # {'height': 40, 'width': 46}

doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(doc_link.text)  # docs.python.org

# Google inspect, right click, copy XPATH
help_link = driver.find_element(By.XPATH, value='//*[@id="container"]/li[1]/ul/li[4]/a')
print(help_link.text)  # Help

driver.quit()  # Quit chrome
