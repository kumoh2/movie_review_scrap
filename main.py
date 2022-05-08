from urllib.request import urlopen
from bs4 import BeautifulSoup
import cx_Oracle
import os

LOCATION = r"/Users/choejaeho/Desktop/oracle" #로컬.
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"] #환경변수 등록

OracleConnect = cx_Oracle.connect("scott/tiger@localhost")
OracleCursor = OracleConnect.cursor()

def no_space(text):
    text2 = text.text.strip()
    return text2

movie_code = 11128
movie_page = 99999

while True:
    while True:
        url = f"https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&page={movie_page}"

        try:
            html = urlopen(url).read()
            soup = BeautifulSoup(html, 'html.parser')
            movie_page = soup.select("input#page")[0]['value']
            score_result = soup.find(class_='score_result')
            li = score_result.find_all('li')
        except:
            movie_page = 99999
            movie_code = int(movie_code) + 1
            str(movie_page)
            str(movie_code)
            break

        for i in range(len(li)):
            usr_id_temp = score_result.li.find_all_next('dt')
            usr_id = usr_id_temp[i].span.text

            review_score_temp = score_result.find_all(class_='star_score')
            review_score = review_score_temp[i].em.text

            review_contents_temp = score_result.li.find_all_next('p')
            review_contents = review_contents_temp[i].span.text.strip()
            review_contents = review_contents.replace("'", "")

            write_date_temp = score_result.find_all(class_='score_reple')
            write_date = write_date_temp[i].em.next_sibling.next_sibling.text

            up_count_temp = score_result.li.a
            up_count = up_count_temp.find_all_next("strong")[2 * i].text

            down_count_temp = score_result.li.a
            down_count = down_count_temp.find_all_next("strong")[2*i+1].text

            oracleSql = f'''
            INSERT INTO movie_review_scrap(movie_code,review_score,review_contents,usr_id,write_date,up_count,down_count)
            VALUES('{movie_code}','{review_score}','{review_contents}','{usr_id}','{write_date}','{up_count}','{down_count}')
            '''

            # print(oracleSql)
            OracleCursor.execute(oracleSql)
            OracleCursor.execute('commit')

            print("영화 :", movie_code)
            print("아이디 :", usr_id)
            print("평점 :",review_score)
            print("리뷰 내용 :", review_contents)
            print("작성 날짜 :", write_date)
            print("공감 숫자 :", up_count)
            print("비공감 숫자 :", down_count)
            print("페이지 넘버 :", movie_page)
            print(i,len(li))
            print("======================")

        movie_page = int(movie_page) - 1
        if movie_page == 0:
            movie_page = 99999
            movie_code = int(movie_code) + 1
        str(movie_page)
        str(movie_code)


