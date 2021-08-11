# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 03:14:35 2021

@author: User
"""
import csv
import json


class output_Result :
    
    #初始化資料
    def __init__(self, model, history) :
        self.model = model
        self.history = history
        self.model_fileName = "captcha_model.hdf5"
        self.history_CSVfileName = "CSV_history.csv"
        self.history_JSONfileName = "JSON_history.json"
        
    def save_model(self) :
        #儲存訓練好的model
        self.model.save(self.model_fileName)

    def save_csv(self) :
        #開啟輸出的csv檔
        with open(self.history_CSVfileName, 'w', newline='') as CSVfile :
            #建立csv檔寫入器
            writer = csv.writer(CSVfile)
            
            writer.writerow(['accuracy'])
            writer.writerow(self.history.history['accuracy'])
            writer.writerow(['val_accuracy'])
            writer.writerow(self.history.history['val_accuracy'])
            writer.writerow(['loss'])
            writer.writerow(self.history.history['loss'])
            writer.writerow(['val_loss'])
            writer.writerow(self.history.history['val_loss'])
        CSVfile.close()
            
    def save_JSON(self) :
        #開啟輸出的json檔
        with open(self.history_JSONfileName, 'w') as JSONfile :
            json.dump('accuracy', JSONfile)
            json.dump(str(self.history.history['accuracy']), JSONfile)
            json.dump('val_accuracy', JSONfile)
            json.dump(str(self.history.history['val_accuracy']), JSONfile)
            json.dump('loss', JSONfile)
            json.dump(str(self.history.history['loss']), JSONfile)
            json.dump('val_loss', JSONfile)
            json.dump(str(self.history.history['val_loss']), JSONfile)
        JSONfile.close()
