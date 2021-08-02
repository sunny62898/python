# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 17:34:59 2021

@author: User
"""

import cv2
import pickle
import os.path
import numpy as np
from imutils import paths
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from helpers import resize_to_fit

letter_images_folder = "extracted_letter_images"
model_fileName = "captcha_model.hdf5"
model_labels_fileName = "model_labels.dat"

#初始化data和labels
data = []
labels = []

#輸入圖片
for image_file in paths.list_images(letter_images_folder) :
    #載入圖片並轉成灰階
    image = cv2.imread(image_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #設定圖片大小為20*20
    image = resize_to_fit(image, 20, 20)
    
    #轉換為nparray為dim = 2
    image = np.expand_dims(image,axis = 2)
    
    #取得label
    label = image_file.split(os.path.sep)[-2]
    
    #增加data和label
    data.append(image)
    labels.append(label)

#處理data的數值控制在0~1之間 所以要/255
data = np.array(data, dtype='float') / 255.0
labels = np.array(labels)

#讀取並分割x_train, x_test, y_train, y_test 等資料
(x_train, x_test, y_train, y_test) = train_test_split(data, labels, test_size=0.25, random_state=0)

#將資料轉為keras可以運作的
lb = LabelBinarizer().fit(y_train)
y_train = lb.transform(y_train)
y_test = lb.transform(y_test)

#儲存model的label
with open(model_labels_fileName, "wb") as f :
    pickle.dump(lb, f)
    
#使用keras建立CNN
model = Sequential()

#建立第一層卷積神經網路
model.add(Conv2D(20, (5,5), padding="same", input_shape=(20,20,1), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

#健力第二層卷積神經網路
model.add(Conv2D(50, (5,5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

#建立隱藏層
model.add(Flatten())
model.add(Dense(500, activation="relu"))

#建立output layer
model.add(Dense(32, activation="softmax"))

#選擇訓練model的compile
model.compile(loss = "categorical_crossentropy",optimizer = "adam", metrics = ["accuracy"])

#開始訓練model
model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=32, epochs=10, verbose=1)

#儲存訓練好的model
model.save(model_fileName)



