# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 22:34:03 2021

@author: User
"""

import numpy as np
from keras.models import load_model
from helpers import resize_to_fit
from imutils import paths
import imutils
import cv2
import pickle
import os.path

model_fileName = "captcha_model.hdf5"
model_labels_fileName = "model_labels.dat"
test_image_folder = "generated_captcha_images"
output_folder = "output_test_images"

#讀取model label
with open(model_labels_fileName, "rb") as f :
    lb = pickle.load(f)
    
#載入已經訓練好的model
model = load_model(model_fileName)

#隨機取圖片來測試
test_images_file = list(paths.list_images(test_image_folder))
test_images_file = np.random.choice(test_images_file, size=(10,), replace=False)

count = 1

#處理隨機選到的圖片
for image_file in test_images_file :
    #讀入並轉成灰階
    image = cv2.imread(image_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #加上額外的padding以便辨識
    image = cv2.copyMakeBorder(image, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
    
    #設置臨界點
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    
    #尋找文字的輪廓
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    #解決不同版本的Opencv
    contours = contours[0] if imutils.is_cv2() else contours[1]
    
    letter_images_regions = []
    
    #搜尋輪廓
    for contour in contours :
        #輪廓的讀取位置以及長寬
        (x, y, w, h) = cv2.boundingRect(contour)
        
        #太寬要分割成兩格
        if w/h > 1.25 :
            half_width = int(w / 2)
            letter_images_regions.append((x, y, half_width, h))
            letter_images_regions.append((x + half_width, y, half_width, h))
            
        else :
            letter_images_regions.append((x, y, w, h))
            
    if len(letter_images_regions) != 4 :
        continue
    
    #讀取letter從左到右
    letter_images_regions = sorted(letter_images_regions, key=lambda x : x[0])
    
    #建立output
    output = cv2.merge([image]*3)
    predicts = []
    
    #loop over letter
    for letter_bounding_box in letter_images_regions :
        #設定座標
        x, y, w, h = letter_bounding_box
        
        #增加2 pixel 的 margin
        letter_image = image[y-2 : y+h+2 , x-2 : x+w+2]
        
        #重新定義圖片大小
        letter_image = resize_to_fit(letter_image, 20, 20)
        
        #轉換為4D
        letter_image = np.expand_dims(letter_image, axis=2)
        letter_image = np.expand_dims(letter_image, axis=0)
        
        #用訓練好的model做預測
        prediction = model.predict(letter_image)
        
        #轉換predict為普通的文字
        letter = lb.inverse_transform(prediction)[0]
        predicts.append(letter)
        
        #畫出預測在圖片上
        cv2.rectangle(output, (x-2, y-2), (x+w+4 , y+h+4), (0, 255, 0), 1)
        cv2.putText(output, letter, (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
        
        
    #print captcha's text
    captcha_text = "".join(predicts)
    print("CAPTCHA text is: {}".format(captcha_text))
    
    #show image
    #cv2.imshow("Output", output)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    
    #存到指定資料夾
    save_path = os.path.join(output_folder)
    #print(save_path)
        
    if not os.path.exists(save_path) :
        os.mkdir(save_path)
        
        
    #寫入輸出圖片
    p = os.path.join(save_path, "output{}.png".format(str(count)))
    cv2.imwrite(p, output)
    
    count = count + 1

