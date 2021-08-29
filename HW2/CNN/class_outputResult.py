# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 23:13:16 2021

@author: User
"""
import csv
import json


class output_Result :
    
    #初始化資料
    def __init__(self, model, history, accuracy, recall, f1, loss) :
        self.model = model
        self.history = history
        self.accuracy = accuracy
        self.recall = recall
        self.f1 = f1
        self.loss = loss
        self.model_fileName = "captcha_model.hdf5"
        self.history_CSVfileName = "CSV_history.csv"
        self.history_JSONfileName = "JSON_history.json"
        self.score_JSONfileName = "JSON_score.json"
        
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
        
    def save_scoreJSON(self) :
        #開啟輸出的json檔
        with open(self.score_JSONfileName, 'w') as score_JSONfile :
            output_acc = "accuracy : " + str(self.accuracy)
            json.dump(output_acc, score_JSONfile)
            output_recall = "recall score : " + str(self.recall)
            json.dump(output_recall, score_JSONfile)
            output_f1 = "f1 score : " + str(self.f1)
            json.dump(output_f1, score_JSONfile)
            output_loss = "loss : " + str(self.loss)
            json.dump(output_loss, score_JSONfile)
        score_JSONfile.close()

