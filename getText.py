from bs4 import BeautifulSoup
import urllib.request
import csv

def get_URL(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL,'html.parser', from_encoding='utf-8')
    URLlist=[]
    for urls in soup.select(".subject > a"):
        if urls["href"].startswith("https://news.mt.co.kr"):
            URLlist.append(urls["href"])
    return URLlist

URL = "https://search.mt.co.kr/searchNewsList.html?srchFd=TOTAL&range=IN&reSrchFlag=&preKwd=&search_type=m&kwd=%BB%EF%BC%BA%C0%FC%C0%DA&bgndt=20180101&enddt=20190930&category=MTNW&sortType=allwordsyn&subYear=&category=MTNW&subType=mt&pageNum="

# 크롤링 함수
def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'html.parser', from_encoding='utf-8')

    text = []
    text.append(soup.select('h1.subject')[0].text)
    text.append(soup.select('.date')[0].get_text()[:11])
    _text = soup.select('#textBody')[0].get_text().replace('\n', " ")
    btext = _text.replace("// flash 오류를 우회하기 위한 함수 추가 function _flash_removeCallback() {}", "")
    text.append(btext.strip())
    return text


# 메인 함수
def main():

    for i in range(544,545):
        f = open('articles'+str(i+1)+'.csv', 'w', encoding='utf-8-sig', newline='')
        wr = csv.writer(f)
        URLlist = get_URL(URL+str(i+1))
        for k in range(15):
            result_text = get_text(URLlist[k])
            wr.writerow(result_text)
        f.close
        print(i + 1)

if __name__ == '__main__':
    main()
