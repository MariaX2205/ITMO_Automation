from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_1():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

try:
    driver.find_elements(By.CSS_SELECTOR, '#login-button')
    driver.find_elements(By.CSS_SELECTOR, '#password')
    driver.find_elements(By.CSS_SELECTOR, '#user-name')
except NoSuchElementException:
    assert False
print("Элементы найдены")




