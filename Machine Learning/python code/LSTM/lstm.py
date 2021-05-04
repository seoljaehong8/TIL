import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation
from keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau
import datetime

data = pd.read_csv('KRW-BTC.csv')
# print(data)

prices = data['close'].values
# print(type(prices))

# 최근 50일 간의 데이터를 보고 내일거를 예측한다.
seq_len = 50
sequence_length = seq_len + 1

result = []
for index in range(len(prices) - sequence_length):
    result.append(prices[index: index + sequence_length])

# print(prices[:51])
# print(result[0])


# 데이터 정규화
# 이유 : 모델이 좀더 잘 예측하게 된다
# 어떻게 정규화? 첫번째 값을 0으로 바꾼다음 나머지를 그비율만큼...?
def normalize_windows(data):
    normalized_data = []
    for window in data:
        normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
        normalized_data.append(normalized_window)
    return np.array(normalized_data)

result = normalize_windows(result)


# 90프로를 training set으로 사용할 것이다.
row = int(round(result.shape[0] * 0.9))
train = result[:row, :]
# 섞어주는게 좀더 정확한 예측 가능
np.random.shuffle(train)

# 학습할 train, 테스트할 test
x_train = train[:, :-1] # 분석할 50개저장
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
y_train = train[:, -1]  # 예측할 1개 저장

x_test = result[row:, :-1]
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
y_test = result[row:, -1]

x_train.shape, x_test.shape


model = Sequential()
# 테스트할 50개
model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))

model.add(LSTM(64, return_sequences=False))
# 예측할 1개
model.add(Dense(1, activation='linear'))
# 손실함수 : mse(Mean Squared Error)
model.compile(loss='mse', optimizer='rmsprop')

model.summary()

start_time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

# training을 시킬거다
model.fit(x_train, y_train,
    validation_data=(x_test, y_test),
    batch_size=10,  # 한번에 몇개씩 묶어서 학습시킬거냐
    epochs=20,      # 20번 동안 반복학습 시킬거다
    callbacks=[
        TensorBoard(log_dir='logs/%s' % (start_time)),
        ModelCheckpoint('./models/%s_eth.h5' % (start_time), monitor='val_loss', verbose=1, save_best_only=True, mode='auto'),
        ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, verbose=1, mode='auto')
])

# 예측하기
pred = model.predict(x_test)

fig = plt.figure(facecolor='white', figsize=(12, 6))
ax = fig.add_subplot(111)
# 실제 데이터
ax.plot(y_test, label='True')
# 예측 데이터
ax.plot(pred, label='Prediction')
ax.legend()
plt.show()
