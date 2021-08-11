# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 03:15:35 2021

@author: User
"""
import os
import os.path
import glob
import cv2
import imutils
from imutils import paths
import numpy as np
from helpers import resize_to_fit


class setData :
    
    #變數初始化
    def __init__(self) :
        self.capture_folder = "generated_captcha_images"
        self.output_folder = "extracted_letter_images"
        
        self.capture_image_file = glob.glob(os.path.join(self.capture_folder,"*"))
        self.counts = {}
        
    #資料處理
    def data_set(self) :
        for (i,image_file) in enumerate(self.capture_image_file) :
            print("[INFO] processing image {}/{}".format(i + 1, len(self.capture_image_file)))
            
            filename = os.path.basename(image_file)
            #print(filename)
            capture_text = os.path.splitext(filename)[0]
            
            
            #下載圖片並轉成灰階
            image = cv2.imread(image_file)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            #增加額外的padding在圖片外
            gray = cv2.copyMakeBorder(gray, 8, 8, 8, 8, cv2.BORDER_REPLICATE)
            
            #設置臨界點(將圖片轉為純黑或純白的pixel)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            
            #找出輪廓
            contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            #相容不同的Opencv版本
            contours = contours[0] if imutils.is_cv2() else contours[1]
            
            letter_image_regions = []
            
            for j in contours :
                
                #取得包含輪廓的位置以及寬高
                (x, y, w, h) = cv2.boundingRect(j)
                
                if w/h > 1.25 :
                    #如果一格太寬要分割成兩格
                    half_wide = int(w/2)
                    letter_image_regions.append((x, y, half_wide, h))
                    letter_image_regions.append((x + half_wide, y, half_wide, h))
                    
                else :
                    letter_image_regions.append((x, y, w, h))
                    
            
            if len(letter_image_regions) != 4 :
                continue
        
            letter_image_regions = sorted(letter_image_regions, key = lambda x : x[0])
        
            for letter_boundingBox, letter_text in zip(letter_image_regions, capture_text) :
                x, y, w, h = letter_boundingBox
                
                letter_image = gray[y - 2:y + h + 2, x - 2:x + w + 2]
                
                #儲存到指定路徑
                save_path = os.path.join(self.output_folder, letter_text)
                #print(save_path)
                
                if not os.path.exists(save_path) :
                    os.mkdir(save_path)
                    
                #寫入output file
                count = self.counts.get(letter_text, 1)
                p = os.path.join(save_path, "{}.png".format(str(count).zfill(6)))
                cv2.imwrite(p, letter_image)
                
                self.counts[letter_text] = count + 1
                    

class change_Data :
    def __init__(self) :
        self.letter_images_folder = "extracted_letter_images"
        
        #初始化data和labels
        self.data = []
        self.labels = []
        
    def input_image(self) :
        #輸入圖片
        for image_file in paths.list_images(self.letter_images_folder) :
            #載入圖片並轉成灰階
            self.image = cv2.imread(image_file)
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            
            #設定圖片大小為20*20
            self.image = resize_to_fit(self.image, 20, 20)
            
            #轉換為nparray為dim = 2
            self.image = np.expand_dims(self.image,axis = 2)
            
            #取得label
            self.label = image_file.split(os.path.sep)[-2]
            
            #增加data和label
            self.data.append(self.image)
            self.labels.append(self.label)
            
    def return_data(self) :
        #處理data的數值控制在0~1之間 所以要/255
        self.data = np.array(self.data, dtype='float') / 255.0
        return self.data
    
    def return_labels(self) :
        #將labels轉為numpy array
        self.labels = np.array(self.labels)
        return self.labels
    