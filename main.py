from urllib.request import urlopen
from bs4 import BeautifulSoup


def no_space(text):
    text2 = text.text.strip()
    return text2

movie_code = 10001
movie_page = 999999

url = f"https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&page={movie_page}"

html = urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

star_score = soup.find(class_='star_score')
score_reple = soup.find(class_='score_reple')
btn_area = soup.find_all(class_='btn_area')

review_score = no_space(star_score.em)
review_contents = no_space(score_reple.span)
usr_id = "test"
write_date = "test"
up_count = "test"
down_count = "test"

print("아이디 :", usr_id)
print("평점 :", review_score)
print("리뷰 내용 :", review_contents)
print("작성 날짜 :", write_date)
print("공감 숫자 :", up_count)
print("비공감 숫자 :", down_count)
print("======================")


