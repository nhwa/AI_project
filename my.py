from Prediction_Util import PredictionUtil
inflation = PredictionUtil()
#모듈을 불러와 객체를 만듭니다.

inflation.read('inflation_data.csv')
inflation.drop('num')
inflation.show()
inflation.lmplot('price_index','bus', 'location')
inflation.lmplot('price_index','taxi','location')
inflation.lmplot('price_index', 'garbagebag', 'location')
inflation.heatmap(['bus','taxi','citygas','waterworks','garbagebag','washing','lodge','haircut','publicbath','Kimchi-jjigae','price_index'])
inflation.boxplot('Kimchi-jjigae','price_index')
inflation.split()