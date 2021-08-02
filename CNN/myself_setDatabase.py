# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:50:44 2021

@author: User
"""
import os
import os.path
import glob
import cv2
import imutils


capture_folder = "generated_captcha_images"
output_folder = "extracted_letter_images"

capture_image_file = glob.glob(os.path.join(capture_folder,"*"))
counts = {}

for (i,image_file) in enumerate(capture_image_file) :
    print("[INFO] processing image {}/{}".format(i + 1, len(capture_image_file)))
    
    filename = os.path.basename(image_file)
    #print(filename)
    capture_text = os.path.splitext(filename)[0]
    #capture_text = os.path.split(filename)[0]  會無法正確分割
    #print(capture_text)
    
    
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
        save_path = os.path.join(output_folder, letter_text)
        #print(save_path)
        
        if not os.path.exists(save_path) :
            os.mkdir(save_path)
            
        #寫入output file
        count = counts.get(letter_text, 1)
        p = os.path.join(save_path, "{}.png".format(str(count).zfill(6)))
        cv2.imwrite(p, letter_image)
        
        counts[letter_text] = count + 1
            
        
