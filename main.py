from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=10001&page=999999"

html = urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')
html_class = soup.find_all(class_='star_score')

print(html_class)