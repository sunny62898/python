# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:35:39 2021

@author: User
"""

'''
    讀入excel檔並整理資料
    1.欄位整併
    2.欄位調換
    3.欄位處理(如有遇到指定要調換的字要替換掉)
    4.欄位刪除
    5.欄位新增
    6.記錄做過什麼事(誰被新增、刪減、整併、更新)
    7.記錄依某幾個欄位進行排序
    8.多維度轉換
    
    !!!進行過什麼都要記錄!!!
'''

import numpy
import openpyxl

#1 of function
def one(array) :
    while(1) : 
        com = input("請問要合併列還是行(1 => 列 , 2 => 行) : ")
        if com == 1 or com == 2 :
            break
        else : 
            print("請輸入1或2")
    
    row = array.shape[0]
    col = array.shape[1]
    print("請問要整併哪兩個欄位")
    
    #input row
    if com == 1 :
        
        while(1) : 
            Comb1 = int(input("請輸入列(請介於0和" + str(row-1) + "之間) : "))
            if 0 <= Comb1 < row :
                break;
            else : 
                print("請介於0和" + str(row) + "之間")
                
        while(1) : 
            Comb2 = int(input("請輸入列(請介於0和" + str(row-1) + "之間) : "))
            if 0 <= Comb2 < row :
                break;
            else : 
                print("請介於0和" + str(row) + "之間")
                
    #input col
    elif com == 2 :
        
        while(1) : 
            Comb1 = int(input("請輸入列(請介於0和" + str(col-1) + "之間) : "))
            if 0 <= Comb1 < col :
                break;
            else : 
                print("請介於0和" + str(col) + "之間")
        while(1) : 
            Comb2 = int(input("請輸入列(請介於0和" + str(col-1) + "之間) : "))
            if 0 <= Comb2 < col :
                break;
            else : 
                print("請介於0和" + str(col) + "之間")
            
    
    print(array)
    numpy.hstack([array[0],array[1]])
    print(array)
    print(row)
    print(col)
    return combine(array , Comb1 , Comb2 , com)

def combine(array , first , second , com) : 
    
    #row
    if com == 1 :
        newArray = numpy.concatenate([array[first],array[second]] , axis = 1)
        print(newArray)
    #col
    elif com == 2 :
        newArray = numpy.concatenate([array[first],array[second]] , axis = 0)
        print(newArray)
    print("123")




#read file
wb = openpyxl.load_workbook('test0.xlsx')  #讀入excel
wb_data = wb.active

readList = [row for row in wb_data.values]

array = numpy.array(readList , dtype = 'str')

#end of read file 

#change array

#說明
print("請輸入所要想要執行的功能的代號")
print("1 => 整併欄位")
print("2 => 欄位調換")
print("3 => 欄位處理(調換有指定字的欄位)")
print("4 => 欄位刪除")
print("5 => 欄位新增")
print("6 => 依照哪幾個欄位進行排序")
print("7 => 多維度轉換")
print("e => 離開此程式")
command = input("command = ")
while(1) :
    if command == '1' :
        print("整併欄位")
        array = one(array)
    elif command == '2' :
        print("欄位調換")
    elif command == '3' :
        print("欄位處理(調換有指定字的欄位)")
    elif command == '4' :
        print("欄位刪除")
    elif command == '5' :
        print("欄位新增")
    elif command == '6' :
        print("依照哪幾個欄位進行排序")
    elif command == '7' :
        print("多維度轉換")
    elif command == 'e' : 
        print("See you~")
        break
    else : 
        print("input error")
    
    command = input("command = ")
    












