# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 03:16:29 2021

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
from keras.layers import LSTM, Dropout, Flatten, Dense
from keras.optimizers import Adam
from helpers import resize_to_fit


class train_Model :
    
    #初始化x_train, y_train, x_test, y_test
    def __init__(self, data, labels) :
        self.model_fileName = "captcha_model.hdf5"
        self.model_labels_fileName = "model_labels.dat"
        
        #讀取並分割x_train, x_test, y_train, y_test 等資料
        (self.x_train, self.x_test, self.y_train, self.y_test) = train_test_split(data, labels, test_size=0.25, random_state=0)
        
        
    def change_to_keras_set(self) :
        #將資料轉為keras可以運作的
        self.x_train = self.x_train.reshape(-1, 20, 20)
        self.x_test = self.x_test.reshape(-1, 20, 20)
        lb = LabelBinarizer().fit(self.y_train)
        self.y_train = lb.transform(self.y_train)
        self.y_test = lb.transform(self.y_test)
        
        #儲存model的label
        with open(self.model_labels_fileName, "wb") as f :
            pickle.dump(lb, f)
            
    def build_RNN_model(self) :
        #使用keras建立RNN
        model = Sequential()
        
        #建立循環神經網路
        model.add(LSTM(128, batch_input_shape=(None,20,20), unroll=True, activation="sigmoid"))
        
        #建立output layer
        model.add(Dense(32, activation="softmax"))
        
        #選擇訓練model的compile
        model.compile(loss = "categorical_crossentropy",optimizer = 'adam', metrics = ["accuracy"])
        
        #開始訓練model並將訓練過程存到history
        self.history = model.fit(self.x_train, self.y_train, validation_data=(self.x_test, self.y_test), batch_size=128, epochs=20, verbose=1)
        
        #儲存訓練好的model
        #model.save(self.model_fileName)
        self.save_model = model
        
        
        
    def return_model(self) :
        return self.save_model
    
    def return_history(self) :
        return self.history
