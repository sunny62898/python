# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 00:59:41 2021

@author: User
"""



import pickle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score,confusion_matrix,f1_score,recall_score,hamming_loss
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras.models import Model
from keras.layers import Dense,GlobalAveragePooling2D, Dropout
from keras.applications import ResNet50
import numpy as np
from scipy import stats



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
        
        self.x_test = np.concatenate((self.x_test,self.x_test,self.x_test),axis=-1)
        self.x_train = np.concatenate((self.x_train,self.x_train,self.x_train),axis=-1)
        #print(self.x_test)
        
        #儲存model的label
        with open(self.model_labels_fileName, "wb") as f :
            pickle.dump(lb, f)
            
    def build_CNN_model(self) :
        
        
        base_model = ResNet50(weights='imagenet', include_top=False)
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(1024, activation='relu')(x)
        x = Dropout(0.5)(x)
        
        predictions = Dense(32, activation='softmax')(x)
        model = Model(inputs=base_model.input, outputs=predictions)
        print(model.summary())
        
        
        #選擇訓練model的compile
        model.compile(loss = "categorical_crossentropy",optimizer = "adam", metrics = ["accuracy"])
        
        #開始訓練model並將訓練過程存到history
        self.history = model.fit(self.x_train, self.y_train,validation_data=(self.x_test, self.y_test), batch_size=16, epochs=10, verbose=1)
        
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
        self.loss = hamming_loss(test_label, pred_label)
        
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
