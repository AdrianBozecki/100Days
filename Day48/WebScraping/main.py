from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.python.org/")

upcoming_events_date = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget  time')
upcoming_events_name = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget  a')
events = {}
i = 0

for time, name in zip(upcoming_events_date, upcoming_events_name):
    events[i] = {
        'time': time.get_attribute("textContent"),
        'name': name.get_attribute("textContent")
    }
    i += 1


driver.quit()
print(events)