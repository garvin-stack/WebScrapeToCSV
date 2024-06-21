from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Navigate to Amazon
    driver.get("https://www.amazon.com")

    input_element = driver.find_element(By.ID, "twotabsearchtextbox")
    input_element.send_keys("vitamin d supplement" + Keys.ENTER)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
    )

    prices = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")
    fractions = driver.find_elements(By.XPATH, "//span[@class='a-price-fraction']")
    names = driver.find_elements(By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']")
    for price, name, fraction in zip(prices, names, fractions):
        print("Price:", price.text + "." + fraction.text)
        print("Name:", name.text)
        print("---")
        print("x")
finally:
    driver.quit()
