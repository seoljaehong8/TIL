###########################
# 라이브러리 사용
import tensorflow as tf
import pandas as pd
 
###########################
# 1.과거의 데이터를 준비합니다.
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
아이리스 = pd.read_csv(파일경로)
아이리스.head()
 
# 원핫인코딩
# 범주형 데이터만 골라서 원핫 인코딩 해준다.
아이리스 = pd.get_dummies(아이리스)
아이리스.head()
 
# 종속변수, 독립변수
독립 = 아이리스[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
종속 = 아이리스[['품종_setosa', '품종_versicolor', '품종_virginica']]
print(독립.shape, 종속.shape)
 
###########################
# 2. 모델의 구조를 만듭니다
X = tf.keras.layers.Input(shape=[4])

H = tf.keras.layers.Dense(8, activation="swish")(X)
H = tf.keras.layers.Dense(8, activation="swish")(H)
H = tf.keras.layers.Dense(8, activation="swish")(H)
# activation=softmax : 비율을 예측하기 위해
Y = tf.keras.layers.Dense(3, activation='softmax')(H)

model = tf.keras.models.Model(X, Y)
# 분류에 사용하는 loss
# metrics='accuracy' 사람이 보기 편하게 정확도 예측
model.compile(loss='categorical_crossentropy',
              metrics='accuracy')
 
# 모델 구조 확인
model.summary()

###########################
# 3.데이터로 모델을 학습(FIT)합니다.
model.fit(독립, 종속, epochs=1000, verbose=0)
model.fit(독립, 종속, epochs=10)
 
###########################
# 4. 모델을 이용합니다
# 맨 처음 데이터 5개
print(model.predict(독립[:5]))
print(종속[:5])
 
# 맨 마지막 데이터 5개
print(model.predict(독립[-5:]))
print(종속[-5:])
 
###########################
# weights & bias 출력
print(model.get_weights())