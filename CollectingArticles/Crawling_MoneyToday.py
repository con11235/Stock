# 기사를 크롤링하기 위한 모듈들을 임포트합니다.
from bs4 import BeautifulSoup
import urllib.request
import csv

# 크롤링할 기사들의 목록이 뜨는 URL입니다.
# bgndt는 시작날짜, enddt는 종료날짜로 설정합니다.
URL = "https://search.mt.co.kr/searchNewsList.html?srchFd=TOTAL&range=IN&reSrchFlag=&preKwd=&search_type=m&kwd=%BB%EF%BC%BA%C0%FC%C0%DA&bgndt=20200622&enddt=20200625&category=MTNW&sortType=allwordsyn&subYear=&category=MTNW&subType=mt&pageNum="

# 위의 URL 내의 기사 목록으로부터 각 기사들의 URL을 크롤링해옵니다.
def get_URL(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL,'html.parser', from_encoding='utf-8')
    URLlist=[]
    for urls in soup.select(".txt"):
        try:    # 기사의 카테고리에 따라 사회나 정치 분야의 카테고리는 제외하고 크롤링합니다.
            if urls.span.get_text()[:2] != '사회' and urls.span.get_text()[:2] != '정치':
                URLlist.append(urls.a.attrs["href"])
        except:
            print(end='')
    return URLlist



# 기사 본문을 크롤링하는 함수입니다.
def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'html.parser', from_encoding='utf-8')

    text = []
    text.append(soup.select('h1.subject')[0].text)      # 기사의 제목
    text.append(soup.select('.date')[0].get_text())     # 기사의 작성일
    _text = soup.select('#textBody')[0].get_text().replace('\n', " ") 
    btext = _text.replace("// flash 오류를 우회하기 위한 함수 추가 function _flash_removeCallback() {}", "")
    text.append(btext.strip())      # 기사 본문
    return text     # [제목, 작성일, 본문] 순서의 리스트입니다.


# 메인 함수
def main():

    for i in range(250):    # 기사 목록 URL으로부터 기사 목록 페이지가 몇 페이지인지 확인하고 크롤링하고자 하는 페이지의 값을 넣습니다.
        URLlist = get_URL(URL+str(i+1))     # i+1번째 페이지의 기사 목록을 받아옵니다.
        text = []
        for k in range(len(URLlist)):
            result_text = get_text(URLlist[k])  # 각 기사의 본문을 크롤링합니다.
            text.append(result_text)
        f = open('articles_del.csv', 'a', encoding='utf-8-sig', newline='')
        wr = csv.writer(f)
        for line in text:
            wr.writerow(line)   # 기사 정보를 파일에 저장합니다.
        f.close
        print(i + 1)

if __name__ == '__main__':
    main()
