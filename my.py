from Prediction_Util import PredictionUtil
inflation = PredictionUtil()
#모듈을 불러와 객체를 만듭니다.

inflation.read('inflation_data.csv')
# inflation.drop('num')
# inflation.show()
# inflation.lmplot('price_index','bus', 'location')
# inflation.lmplot('price_index','taxi','location')
# inflation.lmplot('price_index', 'kimchi-jjigae', 'location')
# inflation.heatmap(['bus','taxi','citygas','waterworks','garbagebag','washing','lodge','haircut','publicbath','kimchi-jjigae','price_index'])
# inflation.plot_3d('lodge','haircut','price_index')

# inflation.boxplot('taxi','price_index')
# inflation.split()
inflation.run_all(['lodge','haircut'],'price_index')
inflation.run_all(['bus','taxi','citygas','waterworks','garbagebag','washing','lodge','haircut','publicbath','kimchi-jjigae'],'price_index')