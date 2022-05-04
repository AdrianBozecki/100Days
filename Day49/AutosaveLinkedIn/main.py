from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


chromedriver_path = Service("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe")
driver = webdriver.Chrome(service=chromedriver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&geoId=103263110&keywords=python%20developer&location=Krak%C3%B3w%2C%20Woj.%20Ma%C5%82opolskie%2C%20Polska")

# Auto Log IN
# **********************************************************
first_log_in_button = driver.find_element(by=By.XPATH, value="/html/body/div[3]/header/nav/div/a[2]")
first_log_in_button.click()

email_input = driver.find_element(by=By.NAME, value="session_key")
email_input.send_keys("")

password_input = driver.find_element(by=By.NAME, value="session_password")
password_input.send_keys("")

second_log_in_button = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
second_log_in_button.click()
# **********************************************************
sleep(2)
job_offer = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container__metadata-item")

for single_offer in job_offer:
    try:
        single_offer.click()
        sleep(2)
        save_job_offer = driver.find_element(by=By.CSS_SELECTOR, value='.jobs-save-button')
        save_job_offer.click()
    except NoSuchElementException:
        print("Exception handled. No such element exception")
        driver.quit()


