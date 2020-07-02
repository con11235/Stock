# 데이터분석캡스톤디자인 6팀 Stock (박승혜, 이상윤)

## 실행 코드 설명

> 1. 데이터의 크롤링 > [CollectingArticles 폴더](https://github.com/con11235/Stock/tree/master/CollectingArticles)
- [Crawling_Mk.ipynb](https://github.com/con11235/Stock/blob/master/CollectingArticles/Crawling_Mk.ipynb) : 매일경제의 기사를 크롤링하는 파일입니다.
- [Crawling_MoneyToday.py](https://github.com/con11235/Stock/blob/master/CollectingArticles/Crawling_MoneyToday.py) : 머니투데이의 기사를 크롤링하는 파일입니다.

> 2. 데이터 전처리 및 생성 > [Preprocessing 폴더](https://github.com/con11235/Stock/tree/master/Preprocessing)
- [make_dataset.ipynb](https://github.com/con11235/Stock/blob/master/Preprocessing/make_dataset.ipynb) : 기사 본문 csv를 불러와 토크나이즈화 한 후 저장합니다. 불러온 데이터를 셔플하는 과정을 거칩니다. 여기서 주가 라벨링 기준을 결정하고 기사 날짜에 맞춰 라벨링 결과를 함께 저장합니다.
- [make_xy_data.ipynb](https://github.com/con11235/Stock/blob/master/Preprocessing/make_xy_data.ipynb) : 위에서 생성한 training과 test파일을 사용하여 단어 수와 제거할 품사, 정규화 여부를설정한 뒤, 모델에 넣기 알맞은 x,y 자료형태로 변환하여 저장합니다.
- [summarize.ipynb](https://github.com/con11235/Stock/blob/master/Preprocessing/summarize.ipynb) : Textrank를 사용하여 본문을 요약하는 코드입니다.

> 3. 데이터 생성에 필요한 csv파일 > [data 폴더](https://github.com/con11235/Stock/tree/master/data)
- [all_200601200619.csv](https://github.com/con11235/Stock/blob/master/data/all_200601200619.csv) : 20년 6월 1일부터 19일까지의 매일경제와 머니투데이의 기사 자료입니다.
- [all_200601200625.csv](https://github.com/con11235/Stock/blob/master/data/all_200601200625.csv) : 20년 6월 1일부터 25일까지의 매일경제와 머니투데이의 기사 자료입니다.
- [maekyung_190101200531.csv](https://github.com/con11235/Stock/blob/master/data/maekyung_190101200531.csv) : 19년 1월 1일부터 20년 5월 31일까지의 매일경제 기사 자료입니다.
- [money_190101200531.csv](https://github.com/con11235/Stock/blob/master/data/money_190101200531.csv) : 19년 1월 1일부터 20년 5월 31일까지의 머니투데이의 기사 자료입니다.
- [stock.csv](https://github.com/con11235/Stock/blob/master/data/stock.csv) : 18년 1월 1일부터 20년 6월 25일까지의 주가 정보입니다. [날짜, 종가, 시가, 고가, 저가, 거래량, 등락율, 전날 날짜, 다음날 날짜, 전일 시가 대비 당일 시가 등락율, 당일 시가 대비 당일 종가 등락율]의 값입니다.

> 4. 모델 비교 > [ComparingConfiguration 폴더](https://github.com/con11235/Stock/tree/master/ComparingConfiguration)
- [DNN(3)-40%요약후'삼성전자'있는 기사만 학습.ipynb](https://github.com/con11235/Stock/blob/master/ComparingConfiguration/DNN(3)-%2040%25%20%EC%9A%94%EC%95%BD%20%ED%9B%84%20'%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90'%20%EC%9E%88%EB%8A%94%20%EA%B8%B0%EC%82%AC%EB%A7%8C%20%ED%95%99%EC%8A%B5.ipynb) : Textrank를 사용한 요약본의 학습 모델입니다.
- [DNN-BatchNormalize.ipynb](https://github.com/con11235/Stock/blob/master/ComparingConfiguration/DNN-BatchNormalize.ipynb) : 데이터 타입 8의 데이터 중 정규화를 하지 않은 데이터를 가지고 모델의 각 레이어 사이에 배치정규화를 추가하여 학습한 모델입니다.
- [DNN-당일 기사 합쳐서 학습.ipynb](https://github.com/con11235/Stock/blob/master/ComparingConfiguration/DNN-%EB%8B%B9%EC%9D%BC%20%EA%B8%B0%EC%82%AC%20%ED%95%A9%EC%B3%90%EC%84%9C%20%ED%95%99%EC%8A%B5.ipynb) : 같은 날짜에 작성된 기사를 모두 합쳐서 학습한 모델입니다.
- [DNN-주말기사를 월요일 기사로 취급.ipynb](https://github.com/con11235/Stock/blob/master/ComparingConfiguration/DNN-%EC%A3%BC%EB%A7%90%EA%B8%B0%EC%82%AC%EB%A5%BC%20%EC%9B%94%EC%9A%94%EC%9D%BC%20%EA%B8%B0%EC%82%AC%EB%A1%9C%20%EC%B7%A8%EA%B8%89.ipynb) : 주말에 작성된 기사를 월요일의 주가로 라벨링하여 데이터에 포함시켜 학습한 모델입니다.
- [optimizer_test.ipynb](https://github.com/con11235/Stock/blob/master/ComparingConfiguration/optimizer_test.ipynb) : 모델 별로 옵티마이저를 변경하여 비교한 모델입니다. RMSprop, Adagrad, Adam, Nadam에 대한 학습 정보를 확인할 수 있습니다.  
#### [단어 수 비교 폴더](https://github.com/con11235/Stock/tree/master/ComparingConfiguration/%EB%8B%A8%EC%96%B4%20%EC%88%98%20%EB%B9%84%EA%B5%90)
- DNN(8)-단어수6000.ipynb~8000.ipynb : 18년 1월 1일부터 19년 9월 30일의 데이터를 가지고 머니투데이를 학습, 매일경제를 테스트 데이터로 (데이터 타입 : 8) 사용하였습니다. 각 단어 수의 epoch별 정확도와 학습 그래프를 확인할 수 있습니다.
- DNN-단어수50000.ipynb : 18년 1월 1일부터 19년 9월 30일의 데이터 중 8의 데이터보다 정제된 데이터(데이터타입 : 15)를 사용하였습니다.  
#### [품사 제거 비교 폴더](https://github.com/con11235/Stock/tree/master/ComparingConfiguration/%ED%92%88%EC%82%AC%20%EC%A0%9C%EA%B1%B0%20%EB%B9%84%EA%B5%90)   
: 각각의 파일명에 제시된 품사들을 제외한 파일들입니다. 외래어, 부사, 한글자 짜리 단어 제거의 경우 ipynb 파일이 삭제되어 결과 데이터를 첨부합니다.

> 5. 최종 결과 및 시각화 > [final result 폴더](https://github.com/con11235/Stock/tree/master/final%20result)
- [DNN-19 학습.ipynb](https://github.com/con11235/Stock/blob/master/final%20result/DNN-19%20%ED%95%99%EC%8A%B5.ipynb) : 최종 목적이었던 19년 1월 1일부터 20년 5월 31일의 데이터를 사용하여 학습하고 20년 6월 1일부터 25일의 데이터를 사용하여 테스트하는 모델입니다.
- [DNN19-예측결과_그래프](https://github.com/con11235/Stock/blob/master/final%20result/DNN19-%EC%98%88%EC%B8%A1%EA%B2%B0%EA%B3%BC_%EA%B7%B8%EB%9E%98%ED%94%84.ipynb) : 위의 데이터타입 19의 6월 예측 결과 정확도와 시각화 그래프를 확인할 수 있습니다.
- [training_money_190101200531_test_maekyung_190101200531.ipynb](https://github.com/con11235/Stock/blob/master/final%20result/training_money_190101200531_test_maekyung_190101200531.ipynb) : 19년 1월 1일부터 20년 5월 31일의 데이터 중 머니투데이의 데이터를 사용하여 학습하고, 매일경제의 데이터를 사용하여 테스트한 모델입니다.

> 6. Textrank 사용한 본문 요약에 필요한 파일 > [textrank 폴더](https://github.com/con11235/Stock/tree/master/textrank/textrank)
위 폴더를 통째로 다운받으면 2번에 summarize 파일을 실행하는데 필요한 파일들을 얻을 수 있습니다. 해당 파일 및 summarize.ipynb 파일 내의 일부 코드는 [TextRank 를 이용한 키워드 추출과 핵심 문장 추출 (구현과 실험)](https://lovit.github.io/nlp/2019/04/30/textrank/) 에서 참고하였습니다.


## 모델 비교 실험 결과

> 1. 기본 모델의 예측 결과   

- 단어 수 : 6000  
- 모델 구조 : 3000(relu), 1000(relu), 3(softmax)  
- epochs : 100  
- batch_size : 1000  
- training : 18년 1월 ~ 19년 9월의 머니투데이  
- test : 18년 1월 ~ 19년 9월의 매일경제  

![](https://i.ibb.co/VgLfmdf/image02.png)  

위의 조건으로 예측을 진행한 결과, 데이터의 정제를 모두 마친 **가장 기본적인 모델의 정확도는 0.77**이다.

> 2. 단어 수 및 epoch의 비교

위의 기본 모델 loss, accuracy 그래프를 참고하면 epoch가 60이 되기 전에는 과적합이 이루어지기 이전, 즉 모델을 학습 중인 상황이므로 멈추지 않고, 60 이후의 값을 20 간격으로 비교하였다. 단어 수 마다 최적의 epoch가 다를 수 있으므로 모든 단어 수에 대해 학습을 진행하였다.

 . | 100 | 80 | 60
---- | ---- | ---- | ----
5000 | 0.7788235 | 0.7647059 | 0.76
6000 | 0.7764706 | 0.7858824 | 0.7929412
7000 | 0.7811764 | 0.7647059 | 0.76
8000 | 0.7905882 | 0.7670588 | 0.7741176

각 단어 수 별로 epoch를 비교해본 결과, **6000개 단어의 60 epoch인 경우가 가장 높은 정확도**를 보였다.
이후 단어의 숫자가 전체 단어 수에 비해 매우 작아서 학습이 원활이 이루어지지 않는 것인지를 확인하기 위해 50000개의 상위 단어를 선정하여 학습하였다. 그 결과 6000개의 단어는 0.7929412의 정확도를 보이는 반면 50000개의 단어는 0.7838617의 정확도로 6000개에 비해 떨어지는 결과를 보였다. 이로 미루어 보았을 때, 단어 수를 매우 크게 잡더라도 **10000번째 이후의 단어들은 등장하는 빈도수 자체가 낮아 모델의 학습에 큰 영향을 미치지 못하는 것**으로 판단하였다.

> 3. 특정 품사 제거  

위의 단어 수 및 에포크 비교로부터 특정 품사 제거 비교에 대한 다음과 같은 기본 형식을 사용하여 비교를 진행하였다.
- 단어 수 : 6000
- 모델 구조 : 3000(relu), 1000(relu), 3(softmax)
- epochs : 60
- batch_size : 1000  

그 결과 각 경우의 정확도는 다음과 같이 계산되었다.
- 제외 단어 없음 : 0.7929412
- Conjunction 제외 : 0.7529412
- Number 제외 : 0.7882353
- Suffix 제외 : 0.7835294
- Foreign 제외 : 0.7882353
- 한 글자 짜리 단어 제외 : 0.7882353
- 부사 제외 : 0.7647059  

비교 결과, **품사를 제거할수록 오히려 제외하지 않은 것에 비해 정확도가 떨어지는 것**을 알 수 있다. 주가와 연관성이 떨어지는 단어일 것이라고 생각하였더라도 품사를 제외할수록 의미 있는 단어들도 같이 제외되기 떄문에 성능이 떨어졌다고 분석하였다.

> 4. TextRank를 사용한 요약 본문 사용

각 기사마다 TextRank를 사용하여 상위 40%의 중요도를 갖는 순서로 문장을 요약하였고, 이 데이터를 사용하여 모델 학습을 진행하였다. 데이터 변화 이외에 모델의 형식은 품사 제거와 같은 기본 형식을 사용하였다. 그 결과 요약 전의 모델은 0.7929412의 정확도를 냈으나, 요약문의 경우 0.7505882의 정확도가 나와 **요약 전이 더 좋은 결과**를 내었다고 결론지었다.

> 5. optimizer의 비교

optimizer의 경우 BoW 기법을 사용할 때 주로 사용되는 RMSprop을 기준으로 학습하였으나, 다른 optimizer를 사용하였을 때 더 좋은 결과를 내는지 확인하기 위한 비교를 진행하였다.
모델 형식은 품사 제거의 경우에 사용한 기본 형식을 사용하였고, 데이터는 추가적인 정제를 거쳤기 때문에 RMSprop까지 다시 학습하여 비교하였다.
- Adagrad : 0.3400576
- RMSprop : 0.8097982
- Adam : 0.7463977
- Nadam : 0.7723343  

그 결과는 위와 같이, RMSprop이 가장 높은 결과를 내었고, Adagrad는 학습율을 조절하여도 크게 나아지지 않는 것을 보아 BoW기법에는 잘 맞지 않는다는 결론을 내었다. 이외에는 Adam보다는 Nadam이 조금 더 개선된 결과를 보였으나 기존에 사용하였던 **RMSprop이 더 높은 정확도**를 보였다.

> 6. batch_normalize
배치 노말라이즈가 모델의 과적합을 막아주기 위한 수단이라고 하여 이를 사용해보았지만, 결과는 정확도 0.6494118로 좋지 않았다.
    
![](https://i.ibb.co/VgLfmdf/image02.png)
![](https://i.ibb.co/L5BS7tW/image04.png)

후자의 그래프가 batch normalize를 사용한 그래프인데, 보면 트레이닝의 경우에는 학습이 매끄럽게 잘 되었음을 알 수 있다. 그러나 **val loss의 개형이 상당히 안정적이지 못함**을 알 수 있고, 때문에 **test의 결과가 좋지 않았을 것**이라고 판단하였다.

> 7. 주말 기사의 처리  

기존에 금요일에서 월요일로 넘어가는 기간의 경우 해당 시간에 발생하는 모든 기사를 취급한 것이 아닌, 월요일에 발생한 데이터만을 가지고 학습을 진행하였다. 그러하여 주말에 작성된 기사들은 모델의 학습에 빠져있었으나, 발생한 시간을 생각해보면 주말의 기사들은 월요일 기사에 영향을 미칠 수도 있다고 생각할 수 있다. 따라서 주말 기사를 월요일 주가로 매치하여 학습한 결과, 정확도는 0.78097982가 나왔다. 기존의 6000개 단어 60 epoch가 79%가 나왔음을 고려하면 **주말의 기사가 월요일의 주가를 결정하기까지 하루 내지 이틀의 시간이 걸리기 때문에 제대로 된 상관관계를 형성하지 못한다**고 결론지었다.

> 8. SVM을 사용한 주가 등락 분류

**rbf kernel을 사용**한 경우, C를 20부터 100 사이, 20 간격으로 설정하고 gamma는 10부터 50 사이, 10 간격으로 설정하여 확인하였을 때, 60 이후부터 train 데이터의 정확도가 95% 이상으로 올라갔다. 따라서 C를 60, 80, 100으로 두고 각 C에 대한 gamma값의 변화에 따른 test 데이터의 정확도를 비교했다. 그 결과 모든 C에 대해 **정확도가 최대 57.3%** 에서 증가하지 않았다.  
**poly kernel을 사용**한 경우, C가 140, 160이고 gamma가 70이상일 때 train 데이터의 정확도가 95% 이상으로 올라갔다. 따라서 C를 140, 160으로 하고 각 C에 대한 gamma값의 변화에 따른 test 데이터의 정확도를 비교했다. 그 결과 모든 C에 대해 **정확도가 최대 57.9%** 에서 증가하지 않았다.  
모델 학습 결과, C와 gamma는 최대 정확도에 도달하기 위한 수단에 불과하며, 최대 정확도를 결정하는 파라미터는 kernel이며, 결국 **두 kernel이 모두 DNN 방식인 80%에 비해 현저히 낮은 정확도를 보였음**을 알 수 있었다. 6000차원의 산점도를 분류할 때 일정 오차를 허용하게 되고, 경계의 모양이 직선, 폐곡선, 개곡선인지의 여부와 관계 없이 결국에는 이러한 점들은 기하학적으로 분류하기에는 **SVM은 데이터 자체에서 영향을 주는 특성과 주지 않는 특성을 구분하는 것이 한계**가 있다. 따라서 DNN 방식이 더 효과적인 모델이었다는 결론이 나왔다.

## [최종 결과물 주요 특징 및 설명](https://github.com/con11235/Stock/tree/master/final%20result)

최종 결과물은 2019년도 1월 1일부터 2020년도 5월 31일까지의 머니투데이 기사를 트레이닝으로, 매일경제 기사를 테스트로 하여 학습해본 결과와, 해당날짜의 두 신문사의 기사들을 모두 트레이닝으로 사용하고 2020년도 6월의 주가 등락율을 예측해보는 것으로 나누었다. 첫 번째 경우는 약 0.7809798이 나왔고, **대부분의 정확도가 학습 상황에 따라 78~80% 사이에 머무름**을 알 수 있었다.  
두 번째 경우는 약 84%의 정확도가 나왔는데, 기간이 짧은 만큼 정확도보다는 각 날짜의 예측 확률과, 실제 주가 등락율을 그래프화 하여 비교하기로 하였다.

[![](https://i.ibb.co/X8HLNFt/image05.png)
![](https://i.ibb.co/47yTVJw/image06.png)](https://github.com/con11235/Stock/blob/master/final%20result/DNN19-%EC%98%88%EC%B8%A1%EA%B2%B0%EA%B3%BC_%EA%B7%B8%EB%9E%98%ED%94%84.ipynb)

각 주가 변동성(상승,유지,하락)에 대한 예측 확률이 각각 파랑, 초록, 빨간색으로 나타내어졌고 가장 넓은 구간을 차지하는 변동성이 해당 날에 예측이 된 주가 변동성이 된다. 그래프 중심부의 회색 선은 주가 등락의 기준이 되는 상한과 하한을 나타낸 선이다. 검은색 점이 실제로 주가 등락율으로 회색선보다 위에있으면 상승, 아래에 있으면 하락, 사이에 있으면 유지로 라벨링 되었다. **초록색의 구간이 어디에 위치하는지를 확인하면 예측 결과를 쉽게 파악**할 수 있었다.   
유지구간이 위쪽에 위치하고 있는 1,3,5,9,16,19,24일의 경우 주가가 상승할 것이라고 예측하였고, 실제로도 상승하였다. 유지구간이 아래쪽에 위치하고 있는 8,11,12,15,25일의 경우 주가가 하락할 것이라고 예측하였고, 실제로도 하락하였다. 유지구간의 구간이 넓게 분포된 2,4,10,17일의 경우 주가가 유지될 것이라고 예측하였고 실제로도 유지되었다. 예측에 실패한 날짜는 18,22,23일으로 18일의 경우 하락할 것이라고 예측되었으나 실제로는 유지되었고, 22,23일의 경우 상승할 것이라고 예측하였으나 실제로는 하락하였다.
