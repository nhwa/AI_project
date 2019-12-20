# AI_project
"지역별 서비스가격을 통한 물가 순위 예측"

< 데이터 출처 >

소비자물가지수동향 
http://kostat.go.kr/incomeNcpi/cpi/cpi_td/2/4/index.action?bmode=cpidtvalregion&region=T10&dtvalsl=rdtval
한국소비자원참가격 서비스가격정보
http://www.price.go.kr/tprice/portal/servicepriceinfo/serviceindustryprice/serviceIndustryPriceList.do
이 사이트들을 참고하여 도시별 서비스가격과 물가순위를 csv 데이터로 만들었습니다.

```python
from Prediction_Util import PredictionUtil
inflation = PredictionUtil()
```
모듈을 불러와 객체를 만듭니다.
