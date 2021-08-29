# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 03:03:12 2021

@author: User
"""


import class_setData
from class_setData import setData
from class_setData import change_Data

import class_trainModel
from class_trainModel import train_Model

#import class_trainModel_new
#from class_trainModel_new import train_Model

import class_outputResult
from class_outputResult import output_Result

class main_function :
    def begain(self) :
        self.data()
        
    def data(self) :
        #資料處理
        set_data = setData()
        set_data.data_set()
        
        change_data = change_Data()
        change_data.input_image()
        self.data = change_data.return_data()
        self.labels = change_data.return_labels()
        
        #run train
        self.train()
        
    def train(self) :
        #training model
        train_model = train_Model(self.data, self.labels)
        train_model.change_to_keras_set()
        train_model.build_RNN_model()
        self.history = train_model.return_history()
        self.model = train_model.return_model()
        self.accuracy, self.recall, self.f1, self.loss = train_model.return_score()
        
        #run result
        self.result()
        
    def result(self) :
        #output result
        output_result = output_Result(self.model, self.history, self.accuracy, self.recall, self.f1, self.loss)
        output_result.save_model()
        output_result.save_csv()
        output_result.save_JSON()
        output_result.save_scoreJSON()

run_main = main_function()
run_main.begain()

