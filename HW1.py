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
        if com == '1' or com == '2' :
            break
        else : 
            print("請輸入1或2")
    
    row = array.shape[0]
    col = array.shape[1]
    #row = len(array)
    #col = len(array[0])
    
    print("請問要整併哪兩個欄位")
    
    #input row
    if com == '1' :
        
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
    elif com == '2' :
        
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
            
    
    
    return combine(array , Comb1 , Comb2 , com)

def combine(array , first , second , com) : 
    
    #計算行數列數
    rows , cols = array.shape
    
    #rows = len(array)
    #cols = len(array[0])
    print(rows)
    print(cols)
    
    print(type(rows))
    print(type(first))
    
    print(array)
    #row
    #指定列 => 跑行
    if com == '1' :
        newArray = numpy.empty([rows - 1 , cols], dtype = ('object'))
        for i in range(cols) : 
            if first == rows-1 :
                newArray[rows - 2 , i] =  array[first , i]+ array[second , i]
            else :
                newArray[first , i] =  array[first , i]+ array[second , i]
            
        print(array)
        
        #刪掉被併掉的那行
        k = 0
        
        #前面重複的
        while(k < second) :
            if k != first :
                for i in range(cols) : 
                    newArray[k , i] = array[k , i]
        
            k = k+1
            
        #後面往前位移的
        p = second
        while(p < rows - 2) :
            for i in range(cols) : 
                newArray[p , i] = array[p+1 , i]
        
            p = p+1
        
        print(str(newArray))
        print(type(newArray[0,1]))
        #print(newArray)
        return newArray
    
    
    #col
    #指定行 => 跑列
    elif com == '2' :
        newArray = numpy.concatenate([array[first],array[second]] , axis = 0)
        print(newArray)
    print("123")




#read file
wb = openpyxl.load_workbook('test0.xlsx')  #讀入excel
wb_data = wb.active

readList = [row for row in wb_data.values]

array = numpy.array(readList , dtype=('str'))

print(type(readList[0][1]))

print(array)

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
    












