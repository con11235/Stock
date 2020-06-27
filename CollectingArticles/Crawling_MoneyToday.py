from bs4 import BeautifulSoup
import urllib.request
import csv

def get_URL(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL,'html.parser', from_encoding='utf-8')
    URLlist=[]
    for urls in soup.select(".txt"):
        try:
            if urls.span.get_text()[:2] != '사회' and urls.span.get_text()[:2] != '정치':
                URLlist.append(urls.a.attrs["href"])
        except:
            print(end='')
    return URLlist

URL = "https://search.mt.co.kr/searchNewsList.html?srchFd=TOTAL&range=IN&reSrchFlag=&preKwd=&search_type=m&kwd=%BB%EF%BC%BA%C0%FC%C0%DA&bgndt=20200622&enddt=20200625&category=MTNW&sortType=allwordsyn&subYear=&category=MTNW&subType=mt&pageNum="

# 크롤링 함수
def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'html.parser', from_encoding='utf-8')

    text = []
    text.append(soup.select('h1.subject')[0].text)
    text.append(soup.select('.date')[0].get_text())
    _text = soup.select('#textBody')[0].get_text().replace('\n', " ")
    btext = _text.replace("// flash 오류를 우회하기 위한 함수 추가 function _flash_removeCallback() {}", "")
    text.append(btext.strip())
    return text


# 메인 함수
def main():

    for i in range(5):
        URLlist = get_URL(URL+str(i+1))
        text = []
        for k in range(len(URLlist)):
            result_text = get_text(URLlist[k])
            text.append(result_text)
        f = open('articles_del.csv', 'a', encoding='utf-8-sig', newline='')
        wr = csv.writer(f)
        for line in text:
            wr.writerow(line)
        f.close
        print(i + 1)

if __name__ == '__main__':
    main()
