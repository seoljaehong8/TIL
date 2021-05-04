import tensorflow as tf
from keras.models import Model
from keras.layers import Dense, Input

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###########################
#
train_data_set = np.arange(0,1000,1)
# 학습할 데이터(문제), 비교할 데이터(답지)
x_train, y_train = [], []

# 20개를 넣어서 다음걸 예측
for i in range(len(train_data_set)-20):
    # 20개씩 각 인덱스에 저장
    x_train.append(train_data_set[i:i+20])
    # 20개 다음 값을 저장
    y_train.append(train_data_set[i+20])

# numpy 기반의 array 로 바꾼다.
x_train = np.array(x_train)
y_train = np.array(y_train)

# print(x_train)

# shape : array의 구조
print(x_train.shape, y_train.shape)

# 학습시킨 걸 가지고 1000~1200 예측 할거다.
test_data_set = np.arange(1000,1200,1)
x_test, y_test = [], []

for i in range(len(test_data_set)-20):
    x_test.append(test_data_set[i:i+20])
    y_test.append(test_data_set[i+20])

x_test = np.array(x_test)
y_test = np.array(y_test)


print(x_test.shape, y_test.shape)


###########################
# 모델을 만듭니다.

# x_train.shape = (980,20)
input_layer = Input(shape=(x_train.shape[1]))

# 히든레이어
# 30개의 신경을 만든다.
# 많다고 잘 되지는 않는다.
# 20개 세트를 30개에 다 넣는다.
# 30개 계산된 결과를 20개에 각각 넣어
# 20개 계산된 결과를 10개에 각각 넣어
dense_layer_1 = Dense(30)(input_layer)
dense_layer_2 = Dense(20)(dense_layer_1)
dense_layer_3 = Dense(10)(dense_layer_2)

# 한가지 값만 나와야 하니까 마지막  한개
output_layer = Dense(1)(dense_layer_3)

# 모델 만들기 (빌드)
model = Model (input_layer,output_layer)

# optimizer : loss를 가지고 어떤 방식으로 가중치를 수정할지 방법론 (컴파일)
model.compile(optimizer='adam', loss='mse')
print(model.summary())


# 모델을 학습시킵니다.
# 전체 데이터를 1000번 반복학습(epochs), 학습진행상황 출력을 끈다 (verbose=0)
model.fit(x_train, y_train, epochs=100, verbose=1)


###########################
# 모델을 이용합니다.
# 얼마나 좋은지 평가를 한다.
model.evaluate(x_test, y_test)

# predict(여기에는 학습한 형태의 데이터와 똑같이 넣어야 한다. 여기서는 20개의 데이터를 넣어야 그에 해당하는 값이 나온다.)
y_hat = model.predict(x_test)
print(y_hat)

plt.figure(figsize = (10,6))
plt.plot(y_hat)
plt.plot(y_test)

plt.show()