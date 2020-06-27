# Stock
데이터분석캡스톤디자인 6팀 Stock 

1. 데이터의 크롤링 > CollectingArticles 폴더
- Crawling_Mk.ipynb : 매일경제의 기사를 크롤링하는 파일입니다.
- Crawling_MoneyToday.py : 머니투데이의 기사를 크롤링하는 파일입니다.

2. 데이터 전처리 및 생성 > Preprocessing 폴더
- make_dataset.ipynb 
: 기사 본문 csv를 불러와 토크나이즈화 한 후 저장합니다. 불러온 데이터를 셔플하는 과정을 거칩니다. 여기서 주가 라벨링 기준을 결정하고 기사 날짜에 맞춰 라벨링 결과를 함께 저장합니다.


3. 데이터 생성에 필요한 csv파일 > data 폴더

4. 모델 비교 > ComparingConfiguration 폴더

5. 최종 결과 및 시각화 > final result 폴더

6. Textrank 사용한 본문 요약에 필요한 파일 > textrank 폴더
위 폴더를 통째로 다운받으면 2번에 summarize 파일을 실행하는데 필요한 파일들을 얻을 수 있습니다.
