# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 01:19:40 2021

@author: User
"""


#example1
import keras
from keras.datasets import mnist
from keras.layers import LSTM
from keras.layers import Dense, Activation
from keras.models import Sequential
from keras.optimizers import Adam


learning_rate = 0.001
training_iters = 20
batch_size = 128
display_step = 10

n_input = 28
n_step = 28
n_hidden = 128
n_classes = 10

(x_train, y_train), (x_test, y_test) = mnist.load_data()

#處理 x_data
x_train = x_train.reshape(-1, n_step, n_input)
x_test = x_test.reshape(-1, n_step, n_input)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train = x_train / 255.0
x_test = x_test / 255.0

#處理 y_data
y_train = keras.utils.to_categorical(y_train, n_classes)
y_test = keras.utils.to_categorical(y_test, n_classes)

#建立RNN model
model = Sequential()

model.add(LSTM(n_hidden, batch_input_shape=(None, n_step, n_input), unroll=True))
model.add(Dense(n_classes))
model.add(Activation('softmax'))

adam = Adam(lr=learning_rate)
model.summary()

model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=batch_size, epochs=training_iters, verbose=1, validation_data=(x_test, y_test))

scores = model.evaluate(x_test, y_test, verbose=0)

print("LSTM test scores : ",scores[0])
print("LSTM test accuracy : ",scores[1])



'''
#example2
import tensorflow as tf
import keras
from keras.datasets import mnist
from keras.layers import Input, Dense, SimpleRNN, RNN, LSTM
from keras.models import Model
import numpy as np
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

sizeOfBatch = 100  #設定一次投入多少的資料量

#建立model
#利用每一層的output在帶入下一層 來達到RNN的效果
inputs = Input(batch_shape=(sizeOfBatch, 28, 28))
RNN1 = SimpleRNN(units=128, activation='tanh', return_sequences=False, return_state=False)
RNN1_output = RNN1(inputs)
Dense1_output = Dense(128, activation='relu')(RNN1_output)
Dense2_output = Dense(128, activation='relu')(Dense1_output)
output = Dense(10, activation='softmax')(Dense2_output)

#將宣告好的模型存到model裡
model = Model(inputs=inputs, outputs=output)

#設定最佳化和編譯器模型
opt = keras.optimizers.Adam(lr=0.001, decay=1e-6)
model.compile(optimizer=opt, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.summary()

#訓練model
model.fit(x_train, y_train, epochs=3, validation_data=(x_test, y_test), batch_size=sizeOfBatch)

#顯示訓練結果
ans = model.predict(x_test[0:100], batch_size=sizeOfBatch)

print("result : ", np.argmax(ans))
'''



