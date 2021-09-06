# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 22:45:12 2021

@author: User
"""

import pickle
import numpy as np
from scipy import stats
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import accuracy_score,confusion_matrix,f1_score,recall_score,log_loss
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense


class train_Model :
    
    #初始化x_train, y_train, x_test, y_test
    def __init__(self, data, labels) :
        self.model_fileName = "captcha_model.hdf5"
        self.model_labels_fileName = "model_labels.dat"
        
        #讀取並分割x_train, x_test, y_train, y_test 等資料
        (self.x_train, self.x_test, self.y_train, self.y_test) = train_test_split(data, labels, test_size=0.25, random_state=0)

    def change_to_keras_set(self) :
        #將資料轉為keras可以運作的
        lb = LabelBinarizer().fit(self.y_train)
        self.y_train = lb.transform(self.y_train)
        self.y_test = lb.transform(self.y_test)
        
        #儲存model的label
        with open(self.model_labels_fileName, "wb") as f :
            pickle.dump(lb, f)
            
    def build_CNN_model(self) :
        #使用keras建立CNN
        model = Sequential()
        
        #建立第一層卷積神經網路
        model.add(Conv2D(20, (5,5), padding="same", input_shape=(20,20,1), activation="relu"))
        model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        
        #建立第二層卷積神經網路
        model.add(Conv2D(50, (5,5), padding="same", activation="relu"))
        model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        
        #建立隱藏層
        model.add(Flatten())
        model.add(Dense(500, activation="relu"))
        
        #建立output layer
        model.add(Dense(32, activation="softmax"))
        
        #選擇訓練model的compile
        model.compile(loss = "categorical_crossentropy",optimizer = "adam", metrics = ["accuracy"])
        
        #開始訓練model並將訓練過程存到history
        self.history = model.fit(self.x_train, self.y_train, validation_data=(self.x_test, self.y_test), batch_size=32, epochs=10, verbose=1)
        
        #儲存訓練好的model
        #model.save(self.model_fileName)
        self.save_model = model
        
        #進入預測function
        self.predict_function()
        
        
    def predict_function(self) : 
        #預測
        predictions = self.save_model.predict(self.x_test)
        pred_label = np.argmax(predictions, axis=1)
        test_label = np.argmax(self.y_test, axis=1)
        
        test_value = t_test(test_label, pred_label)
        test_value.p_value()
        
        self.accuracy = accuracy_score(test_label, pred_label)
        self.recall = recall_score(test_label, pred_label,pos_label='positive',average='micro')
        self.f1 = f1_score(test_label, pred_label,pos_label='positive',average='micro')
        
        proba = self.save_model.predict_proba(self.x_test)
        self.loss = log_loss(test_label, proba)
        
    def return_model(self) :
        return self.save_model
    
    def return_history(self) :
        return self.history
    
    def return_score(self) :
        return self.accuracy, self.recall, self.f1, self.loss

class t_test :
    def __init__(self, ans_label, pred_label) :
        self.answer = ans_label
        self.predict = pred_label
        
    def p_value(self) :
        #sample size
        N = len(self.answer)
        
        var_answer = self.answer.var(ddof=1)
        var_predict = self.predict.var(ddof=1)
        
        print('var_answer : ', var_answer)
        print('var_predict : ', var_predict)
        
        #std deviation
        s = np.sqrt((var_answer+var_predict)/2)
        
        #統計量
        t = (self.answer.mean() - self.predict.mean())/(s*np.sqrt(2/N))
        
        #自由度
        df = 2*N - 2
        
        #計算p-value after comparison with the t
        p = 1 - stats.t.cdf(t,df=df)
        
        print('test p value : ', stats.ttest_ind(self.answer, self.predict, equal_var=False))


