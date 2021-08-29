# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 04:19:46 2021

@author: User
"""

import cv2
import pickle
import os.path
import numpy as np
from imutils import paths
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import accuracy_score,confusion_matrix,f1_score,recall_score, log_loss
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import LSTM, MaxPooling2D, Flatten, Dense
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
        
        #建立第一層循環神經網路
        model.add(LSTM(128, batch_input_shape=(None,20,20), unroll=True, activation="relu"))
        
        #建立隱藏層
        #model.add(Dense(512, activation="sigmoid"))
        #model.add(Dense(100, activation="sigmoid"))
        
        #建立output layer
        model.add(Dense(32, activation="softmax"))
        model.summary()
        
        #選擇訓練model的compile
        model.compile(loss = "categorical_crossentropy",optimizer = 'adam', metrics = ["accuracy"])
        
        #開始訓練model並將訓練過程存到history
        self.history = model.fit(self.x_train, self.y_train, validation_data=(self.x_test, self.y_test), batch_size=128, epochs=10, verbose=1)
        
        #預測
        predictions = model.predict(self.x_test)
        pred_label = np.argmax(predictions, axis=1)
        test_label = np.argmax(predictions, axis=1)
        #print(pred_label)
        #print(test_label)
        #CM = confusion_matrix(test_label, pred_label)
        #print("混淆矩陣 : ", CM)
        print("accuracy score : ", accuracy_score(test_label, pred_label))
        recall = recall_score(test_label, pred_label,pos_label='positive',average='micro')
        f1 = f1_score(test_label, pred_label,pos_label='positive',average='micro')
        print("recall score : ",recall)
        print("f1 score : ",f1)
        
        proba = model.predict_proba(self.x_test)
        #print(proba)
        loss = log_loss(test_label, proba)
        print("log loss : ", loss)
        
        #儲存訓練好的model
        #model.save(self.model_fileName)
        self.save_model = model
        
        #test score
        scores = model.evaluate(self.x_test, self.y_test, verbose=0)

        print("LSTM test scores : ",scores[0])
        print("LSTM test accuracy : ",scores[1])
        
        
    def return_model(self) :
        return self.save_model
    
    def return_history(self) :
        return self.history
