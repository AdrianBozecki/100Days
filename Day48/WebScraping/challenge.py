from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromedriver_path = Service("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe")
driver = webdriver.Chrome(service=chromedriver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
article_count = int(article.get_attribute("textContent").replace(",", ""))

all_portals = driver.find_element(by=By.LINK_TEXT, value="free")

search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# search_button = data.find_element(by=By.NAME, value="go")
# search_button.click()