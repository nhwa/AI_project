from Prediction_Util import PredictionUtil
inflation = PredictionUtil()
#모듈을 불러와 객체를 만듭니다.

inflation.read('inflation_data.csv')
#inflation_data.csv 파일을 읽습니다.

inflation.drop('num')
inflation.show()
# 필요없는 'num' 컬럼을 삭제하고 데이터 유형 및 내용을 확인합니다.

inflation.lmplot('price_index','bus', 'location')
inflation.lmplot('price_index','taxi','location')
inflation.lmplot('price_index', 'kimchi-jjigae', 'location')
# implot으로 그려본 상관관계

inflation.boxplot('taxi','price_index')
# boxplot으로 그려본 상관관계

inflation.plot_3d('lodge','haircut','price_index')
# 3차원으로 그려본 상관관계

inflation.heatmap(['bus','taxi','citygas','waterworks','garbagebag','washing','lodge','haircut','publicbath','kimchi-jjigae','price_index'])
# heatmap으로 그려본 상관관계

inflation.run_all(['lodge'],'price_index')
# lodge만을 사용하여 인식률을 확인합니다.

inflation.run_all(['bus','taxi','citygas','waterworks','garbagebag','washing','lodge','haircut','publicbath','kimchi-jjigae'],'price_index')
# 모든 컬럼을을 사용하여 인식률을 확인합니다.