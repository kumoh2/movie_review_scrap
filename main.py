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
movie_page = soup.select("input#page")[0]['value']

score_result = soup.find(class_='score_result')
li = score_result.find_all('li')

for i in range(len(li)):
    usr_id = score_result.li.find_all_next('dt')
    review_score = score_result.find_all(class_='star_score')
    review_contents = score_result.li.find_all_next('p')
    write_date = score_result.find_all(class_='score_reple')
    up_count = score_result.li.a
    down_count = score_result.li.a

    print("영화 :", movie_code)
    print("아이디 :", usr_id[i].span.text)
    print("평점 :", review_score[i].em.text)
    print("리뷰 내용 :", review_contents[i].span.text.strip())
    print("작성 날짜 :", write_date[i].em.next_sibling.next_sibling.text)
    print("공감 숫자 :", up_count.find_all_next("strong")[2*i].text)
    print("비공감 숫자 :", down_count.find_all_next("strong")[2*i+1].text)
    print("페이지 넘버 :", movie_page)
    print("======================")


