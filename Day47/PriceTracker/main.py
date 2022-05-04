from bs4 import BeautifulSoup
import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7"
}
response = requests.get("https://www.amazon.com/ROCCAT-Vulcan-Compact-Optical-Keyboard/dp/B08J4DGBB9/ref=sr_1_1_sspa?keywords=gaming%2Bkeyboard&pd_rd_r=d81b33b2-0a2f-4248-8b95-e3ac75ddd08d&pd_rd_w=KZpGG&pd_rd_wg=gNzkh&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=E93HPE2MQEG9TMRQ2E0S&qid=1651569519&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFOUFBBNkhMTkxIRTcmZW5jcnlwdGVkSWQ9QTA3OTc5NjMzNTRRWUc5NjVaUlQzJmVuY3J5cHRlZEFkSWQ9QTA4MDE0NTUyRjZaVTkyQktNOFJOJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1", headers = header)
soup = BeautifulSoup(response.text, "html.parser")

price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])
print(price)
