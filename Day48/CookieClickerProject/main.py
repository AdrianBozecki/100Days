from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



chrome_driver_path = Service("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


def buy():
    points = int(driver.find_element(by=By.ID, value="money").get_attribute("textContent").replace(",", ""))
    if points > 123456789:
        id = "buyTime machine"
    elif points > 1000000:
        id = "buyPortal"
    elif points > 50000:
        id = "buyAlchemy lab"
    elif points > 7000:
        id = "buyShipment"
    elif points > 2000:
        id = "buyMine"
    elif points > 500:
        id = "buyFactory"
    elif points > 100:
        id = "buyGrandma"
    elif points > 15:
        id = "buyCursor"

    buy = driver.find_element(by=By.ID, value=id)
    buy.click()


cookie = driver.find_element(by=By.ID, value="cookie")


timeout = time.time() + 5

while True:
    cookie.click()
    if time.time() > timeout:
        buy()
        timeout = time.time() + 5


