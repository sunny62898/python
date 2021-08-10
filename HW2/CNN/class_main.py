# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 21:16:30 2021

@author: User
"""


#import class
import class_setData
from class_setData import setData
from class_setData import change_Data

import class_trainModel
from class_trainModel import train_Model

import class_outputResult
from class_outputResult import output_Result


#資料處理
set_data = setData()
set_data.data_set()

change_data = change_Data()
change_data.input_image()
data = change_data.return_data()
labels = change_data.return_labels()

#training model
train_model = train_Model(data, labels)
train_model.change_to_keras_set()
train_model.build_CNN_model()
history = train_model.return_history()
model = train_model.return_model()


#output result
output_result = output_Result(model, history)
output_result.save_model()
output_result.save_csv()
output_result.save_JSON()





