from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

article_upvote = [int(single_upvote.getText().split()[0]) for single_upvote in soup.find_all(name="span", class_="score")]

highest_upvote_index = article_upvote.index(max(article_upvote))

print(article_texts[highest_upvote_index])
print(article_links[highest_upvote_index])
print(article_upvote[highest_upvote_index])


