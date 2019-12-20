# AI_project
### "지역별 서비스가격을 통한 물가 순위 예측"

#### 데이터 출처

소비자물가지수동향  
http://kostat.go.kr/incomeNcpi/cpi/cpi_td/2/4/index.action?bmode=cpidtvalregion&region=T10&dtvalsl=rdtval

한국소비자원참가격 서비스가격정보
http://www.price.go.kr/tprice/portal/servicepriceinfo/serviceindustryprice/serviceIndustryPriceList.do

이 사이트들을 참고하여 도시별 서비스가격과 물가순위를 csv 데이터로 만들었습니다.


* * *


#### 1. 데이터 불러오기 

```python
from Prediction_Util import PredictionUtil
inflation = PredictionUtil()
```
모듈에 있는 class PredictionUtil을 불러와 객체를 만듭니다.


* * *


#### 2. 객체 생성하기 

```python
inflation.read('inflation_data.csv')
```

inflation_data.csv 파일을 읽습니다.

![1](https://user-images.githubusercontent.com/44343908/71241491-17636580-234f-11ea-85e8-dbfce2c21d6a.PNG)



* * *


#### 3. 데이터 정리하기
```python
inflation.drop('num')
inflation.show()
```

필요없는 'num' 컬럼을 삭제하고 데이터 유형 및 내용을 확인합니다. 

![image](https://user-images.githubusercontent.com/44343908/71241765-c3a54c00-234f-11ea-844b-0d111e4a3d07.png)


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
```python
inflation.lmplot('price_index','bus', 'location')
```

버스요금에 따른 물가지수

![image](https://user-images.githubusercontent.com/44343908/71242576-99548e00-2351-11ea-83e1-09bf69de5709.png)


```python
inflation.lmplot('price_index','taxi','location')
```

택시요금에 따른 물가지수

![image](https://user-images.githubusercontent.com/44343908/71242787-0a944100-2352-11ea-9e44-8c14a29b2407.png)

```python
inflation.lmplot('price_index', 'kimchi-jjigae', 'location')
```

김치찌개에 따른 물가지수

![image](https://user-images.githubusercontent.com/44343908/71242976-87271f80-2352-11ea-94ab-265cdba81a2c.png)





