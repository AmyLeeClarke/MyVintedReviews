from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.vinted.co.uk/member/58931711-gothkawaii")

accept = driver.find_element("xpath", '//*[@id="onetrust-accept-btn-handler"]')
accept.click()

reviews = driver.find_element("xpath", '//*[@id="feedback"]/span/span')
reviews.click()
time.sleep(30)

reviews = driver.find_elements(By.CLASS_NAME, "web_ui__Cell__body")


