# AI_project
### "지역별 서비스가격을 통한 물가 예측"

#### 데이터 출처

소비자물가지수동향  
http://kostat.go.kr/incomeNcpi/cpi/cpi_td/2/4/index.action?bmode=cpidtvalregion&region=T10&dtvalsl=rdtval

한국소비자원참가격 서비스가격정보
http://www.price.go.kr/tprice/portal/servicepriceinfo/serviceindustryprice/serviceIndustryPriceList.do

> 이 사이트들을 참고하여 도시별 서비스가격과 물가순위를 csv 데이터로 만들었습니다.




* * *




#### 1. 데이터 불러오기 

```python
from Prediction_Util import PredictionUtil
inflation = PredictionUtil()
```
> 모듈에 있는 class PredictionUtil을 불러와 객체를 만듭니다.




* * *




#### 2. 객체 생성하기 

```python
inflation.read('inflation_data.csv')
```

> inflation_data.csv 파일을 읽습니다.

<img src="./assets/1.png" alt="1" width="70%"/>




* * *




#### 3. 데이터 정리하기
```python
inflation.drop('num')
inflation.show()
```

> 필요없는 'num' 컬럼을 삭제하고 데이터 유형 및 내용을 확인합니다. 

<img src="./assets/2.png" alt="2" width="70%"/>


location | 지역
----- | -----  
price_index | 물가지수  
bus | 버스요금 
taxi | 택시요금
citygas | 도시가스요금
waterworks | 상수도요금
garbagebag | 쓰레기봉투요금
washing | 세탁비요금
lodge | 숙박요금
haircut | 미용요금
publicbath | 공중목욕탕요금




* * *




#### 4. 데이터 수치화 - 서비스가격에 따른 물가지수 상관관계 파악 

##### implot으로 그려본 상관관계
```python
inflation.lmplot('price_index','bus', 'location')
```

> 버스요금에 따른 물가지수

<img src="./assets/3.png" alt="3" width="70%"/>


```python
inflation.lmplot('price_index','taxi','location')
```

> 택시요금에 따른 물가지수

<img src="./assets/4.png" alt="4" width="70%"/>

```python
inflation.lmplot('price_index', 'kimchi-jjigae', 'location')
```

> 김치찌개에 따른 물가지수

<img src="./assets/5.png" alt="5" width="70%"/>




##### boxplot으로 그려본 상관관계
```python
inflation.boxplot('taxi','price_index')
```

> taxi에 따른 물가지수

<img src="./assets/6.png" alt="6" width="70%"/>




##### 3차원으로 그려본 상관관계
```python
inflation.plot_3d('lodge','haircut','price_index')
```

> lodge,haircut에 따른 물가지수

<img src="./assets/7.png" alt="7" width="70%"/>




##### heatmap으로 그려본 상관관계
```python
inflation.heatmap(['bus','taxi','citygas','waterworks','garbagebag','washing','lodge','haircut','publicbath','kimchi-jjigae','price_index'])
```



>heatmap(열지도)으로 각 컬럼별 상관관계를 표현하였습니다.  

lodge(숙박요금)이 price_index(물가지수)에 가장 많은 영향을 주는 것을 알 수 있습니다.  
haircut(미용요금)이 price_index(물가지수)에 두번째로 영향을 주는 것을 알 수 있습니다.  
*waterworks(상수도 요금)은 price_index(물가지수)에 거의 영향을 끼치지 않습니다.*




* * *




#### 5. 상관관계를 이용하여 물가지수 예측하기 

```python
inflation.run_all(['lodge','haircut'],'price_index')
```

> lodge만을 사용하여 인식률을 확인합니다.

<img src="./assets/9.png" alt="9" width="50%"/>

선형회귀 알고리즘 : 0%  
K-NN 알고리즘 : 11%  
결정트리 알고리즘 : 0%  
랜덤 포레스트 알고리즘 : 0%  


* * *





```python
inflation.run_all(['lodge','haircut'],'price_index')
```

> 모든 컬럼을 사용하여 인식률을 확인합니다.

<img src="./assets/10.png" alt="10" width="50%"/>


선형회귀 알고리즘 : 0%  
K-NN 알고리즘 : 9%  
결정트리 알고리즘 : 0%  
랜덤 포레스트 알고리즘 : 0%  
