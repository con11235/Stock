import csv
import re

f = open('articles002.csv','r',encoding='utf-8')
f2 = open('modified002.csv','w', encoding='utf-8-sig', newline='')
rdf = csv.reader(f)
wrf2 = csv.writer(f2)

for line in rdf:
    text = line[2]
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)' #이메일 주소 제거
    text = re.sub(pattern=pattern, repl=' ',string=text)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'#URL 제거
    text = re.sub(pattern=pattern, repl=' ', string=text)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)' #한글 자모음 제거
    text = re.sub(pattern=pattern, repl=' ', string=text)
    pattern = '[^\w\s]' #특수기호 제거
    text = re.sub(pattern=pattern, repl=' ', string=text)

    index = 0
    while True:
        index = text.find('삼성 ',index+2)
        if index == -1:
            break
        if text[index+3:index+5] == '전자':
            text = text[:index+2] + text[index+3:index+5]

    line[2] = text
    wrf2.writerow(line)


f.close()
f2.close()