# AI_project
### "지역별 서비스가격을 통한 물가 순위 예측"

#### 데이터 출처

소비자물가지수동향
http://kostat.go.kr/incomeNcpi/cpi/cpi_td/2/4/index.action?bmode=cpidtvalregion&region=T10&dtvalsl=rdtval

한국소비자원참가격 서비스가격정보
http://www.price.go.kr/tprice/portal/servicepriceinfo/serviceindustryprice/serviceIndustryPriceList.do

이 사이트들을 참고하여 도시별 서비스가격과 물가순위를 csv 데이터로 만들었습니다.

```python
from Prediction_Util import PredictionUtil
inflation = PredictionUtil()
```
모듈에 있는 class PredictionUtil을 불러와 객체를 만듭니다.

```python
inflation.read('inflation_data.csv')
```
inflation_data.csv 파일을 읽습니다.

|location|지역|
location | 지역
price_index | 물가지수

bus | 버스요금
'taxi' | 택시요금
'citygas' | 도시가스요금
'waterworks' | 상수도요금
'garbagebag' | 쓰레기봉투요금
'washing' | 세탁비요금
'lodge' | 숙박요금
'haircut' | 미용요금
'publicbath' | 공중목욕탕요금
| 내용 11 | 내용 12 |
| 내용 11 | 내용 12 |
| 내용 11 | 내용 12 |
| 내용 11 | 내용 12 |
| 내용 11 | 내용 12 |
| 내용 11 | 내용 12 |
