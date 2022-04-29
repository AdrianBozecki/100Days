from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.imdb.com/chart/top/")
imdb = response.text

soup = BeautifulSoup(imdb, "html.parser")
all_movies = [a.select("a")[0].getText() for a in soup.find_all(name="td", class_="titleColumn")]
all_ratings = [a.select("strong")[0].getText() for a in soup.find_all(name="td", class_="ratingColumn imdbRating")]


top100movies = {}
for i in range(len(all_movies) - 1, -1, -1):
    top100movies[i + 1] = (all_movies[i], all_ratings[i])

print(top100movies)

