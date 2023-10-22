from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name_inp = driver.find_element(By.XPATH, value="/html/body/form/input[1]")
l_name_inp = driver.find_element(By.XPATH, value="/html/body/form/input[2]")
email_inp = driver.find_element(By.XPATH, value="/html/body/form/input[3]")
sign_up_btn = driver.find_element(By.XPATH, value="/html/body/form/button")

f_name_inp.send_keys("Kristian")
l_name_inp.send_keys("Skreosen")
email_inp.send_keys("kristian.skreosen.test@gmail.com")
sign_up_btn.click()
