# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 23:24:40 2021

@author: User
"""

import tensorflow
import keras

import json
import numpy


print(tensorflow.__version__)
print(keras.__version__)
print(tensorflow.test.is_gpu_available())


'''
import tensorflow as tf
mnist = tf.keras.datasets.mnist

# 匯入 MNIST 手寫阿拉伯數字 訓練資料
(x_train, y_train),(x_test, y_test) = mnist.load_data()
# 特徵縮放，使用常態化(Normalization)，公式 = (x - min) / (max - min)
# 顏色範圍：0~255，所以，公式簡化為 x / 255
x_train, x_test = x_train / 255.0, x_test / 255.0

# 建立模型
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

# 設定優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)的類別
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 模型訓練
model.fit(x_train, y_train, epochs=5)
# 模型評估，打分數
model.evaluate(x_test, y_test)
'''