###########################
# 라이브러리 사용
import tensorflow as tf
import pandas as pd
 
###########################
# 데이터를 준비합니다.
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
레모네이드 = pd.read_csv(파일경로)
레모네이드.head()
# 종속변수, 독립변수
독립 = 레모네이드[['온도']]
종속 = 레모네이드[['판매량']]
print(독립.shape, 종속.shape)
 
###########################
# 모델을 만듭니다.
# 우리가 사용할 독립변수 칼럼이 '온도' 한개 이기때문에 shape=[1]
X = tf.keras.layers.Input(shape=[1])
# 우리가 예측할 종속변수 칼럼이 '판매량' 한개 이기때문에 Dense(1)
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')
 
###########################
# 모델을 학습시킵니다. 
# 전체 데이터를 1000번 반복학습(epochs), 학습진행상황 출력을 끈다 (verbose=0)
model.fit(독립, 종속, epochs=10000, verbose=0)
model.fit(독립, 종속, epochs=10)
 
###########################
# 모델을 이용합니다. 
print(model.predict(독립))
print(model.predict([[15]]))