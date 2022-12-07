# import requests
# from bs4 import BeautifulSoup


# for p in range(1, 6):
#     raw = requests.get(
#         "https://series.naver.com/ebook/top100List.nhn?page=" + str(p),
#         headers={"User-Agent": "Mozilla/5.0"},
#     )
#     html = BeautifulSoup(raw.text, "html.parser")

#     books = html.select("div.lst_thum_wrap li")
#     for b in books:
#         title = b.select_one("a strong").text
#         author = b.select_one("span.writer").text
#         price = b.select_one("p.price2").text
#         print(title, author, price)

import urllib.request
import json


def search(title):
    # 애플리케이션 클라이언트 id 및 secret
    client_id = "RT1aMSfJhi4zxmScoQvA"
    client_secret = "XEFURspxqs"

    # 도검색 url
    url = "https://openapi.naver.com/v1/search/book.json"
    query = "?query=" + urllib.parse.quote(title)

    url_query = url + query

    # Open API 검색 요청 개체 설정
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    # 검색 요청 및 처리
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        return response.read().decode("utf-8")
    else:
        return None


# 프로그램 진입점
def main():
    # 검색 질의 요청
    res = search(input("질의:"))
    if res == None:
        print("검색 실패!!!")
        exit()

    # 검색 결과를 json개체로 로딩
    json_response = json.loads(res)
    if json_response == None:
        print("json.loads 실패!!!")
        exit()

    # 검색 결과의 items 목록의 각 항목(post)을 출력
    for item in json_response["items"]:
        print("제목:" + item["title"])
        print("설명:" + item["description"])
        print("가격:" + item["price"])
        print("(" + item["discount"] + ")")
        print("url:" + item["link"])
        print("================\n")


# 진입점 함수를 main으로 지정
if __name__ == "__main__":
    main()
