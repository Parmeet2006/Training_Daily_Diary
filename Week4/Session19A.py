import requests
from bs4 import BeautifulSoup # Web Scrapping (Fetching useful data from HTML)

# url = 'https://www.imdb.com/india/top-rated-indian-movies/'
url = 'https://books.toscrape.com/'

response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# p_tags = soup.find_all('p')
# p_tags = soup.find_all('p', class_='star-rating Three')

a_tags = soup.find_all('a')

for a_tag in a_tags:
    print(a_tag.text)

# Explore - PDF Reader/Writer Library