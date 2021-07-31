# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 14:34:03 2021

@author: User
"""


import tensorflow
from tensorflow import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D
from keras.models import model_from_json
from keras.optimizers import SGD,Adam
import numpy as np
from keras.utils import np_utils

(train_x, train_y),(test_x, test_y) = mnist.load_data()

#print(len(train_x))  #顯示有幾張圖片
#print(train_x[0])  #顯示圖片大小


#初始化np array
train_x = train_x.reshape(train_x.shape[0],28,28,1).astype('float32')
test_x = test_x.reshape(test_x.shape[0],28,28,1).astype('float32')

train_x, test_x = train_x/255.0 , test_x/255.0

train_y = np_utils.to_categorical(train_y)
test_y = np_utils.to_categorical(test_y)

#print(train_x[0])  #顯示圖片大小

#搭建 keras model
model = Sequential()

#第一層
model.add(Conv2D(filters = 16, kernel_size = (5,5), padding = 'same', input_shape = (28, 28, 1), activation = 'relu'))

model.add(MaxPooling2D(pool_size=(2,2)))

#第二層
model.add(Conv2D(filters = 36, kernel_size = (5,5), padding = 'same', activation = 'relu'))

model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))  #避免overfitting

model.add(Flatten())  #建立平坦層
model.add(Dense(128, activation='relu'))  #建立隱藏層

model.add(Dropout(0.5))

#建立輸出層
model.add(Dense(10, activation='softmax'))

print(model.summary())  #顯示model的細節




'''
#簡單但精準度較低
#初始化np array
train_x = train_x.reshape(train_x.shape[0],28*28).astype('float32')
test_x = test_x.reshape(test_x.shape[0],28*28).astype('float32')

train_x, test_x = train_x/255.0 , test_x/255.0

train_y = np_utils.to_categorical(train_y,10)
test_y = np_utils.to_categorical(test_y,10)

#print(train_x[0])  #顯示圖片大小


model = Sequential()
model.add(Dense(input_dim=28*28, units=500,activation='relu'))
model.add(Dense(units=500, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
'''

#訓練模型
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics=['accuracy'])
train_history = model.fit(x = train_x, y = train_y, validation_split=0.2, epochs=20, batch_size=300, verbose=2)

#將訓練結果儲存
json_string = model.to_json()
with open("model.json","w") as file :
    file.write(json_string)
    
#儲存權重
model.save_weights("model.weight")




#畫出訓練圖
import matplotlib.pyplot as plt

def save_history(train_acc, test_acc, filename) :
    plt.clf()
    plt.plot(train_history.history[train_acc])
    plt.plot(train_history.history[test_acc])
    plt.title("train history")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(["train","test"], loc = "upper left")
    plt.savefig(filename)
    
save_history('accuracy', 'val_accuracy', 'accuracy.png')
save_history('loss', 'val_loss', 'loss.png')

#評估準確率
score = model.evaluate(test_x, test_y)
score[1]

prediction=model.predict_classes(test_x)
prediction[:10]

