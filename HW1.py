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

'''
function part 
'''
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
    
    
    
    #input row
    if com == '1' :
        print("請問要整併哪兩列")
    
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
        print("請問要整併哪兩行")
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
        print(newArray)
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
        while(p < rows - 1) :
            if first == rows - 1 :
                if p != first-1 :
                    for i in range(cols) : 
                        newArray[p , i] = array[p+1 , i]
            else :
                if p != first :
                    for i in range(cols) : 
                        newArray[p , i] = array[p+1 , i]
            
        
            p = p+1
        
        print(str(first) + "列和" + str(second) + "列已經被整併")
        return newArray
    #end of row
    
    #col
    #指定行 => 跑列
    elif com == '2' :
        newArray = numpy.empty([rows , cols - 1], dtype = ('object'))
        for i in range(rows) : 
            if first == cols - 1 :
                newArray[i , cols - 2] =  array[i , first]+ array[i , second]
            else :
                newArray[i , first] =  array[i , first]+ array[i , second]
            
        print(array)
        
        #刪掉被併掉的那列
        k = 0
        
        #前面重複的
        while(k < second) :
            if k != first :
                for i in range(rows) : 
                    newArray[i , k] = array[i , k]
            k = k+1
        
        
        #後面往前位移的
        p = second
        print(cols - 2)
        
        while(p < cols - 1) :
            if first == cols - 1 :
                if p != first - 1 :
                    for i in range(rows) : 
                        newArray[i , p] = array[i , p+1]
            else :
                if p != first :
                    for i in range(rows) : 
                        newArray[i , p] = array[i , p+1]
            
            p = p+1
            
            
        print(str(first) + "行和" + str(second) + "行已經被整併")
        return newArray
    #end of col
    
#1 of function end

#2 of function
def two(array) :
    while(1) : 
        com = input("請問要對調列還是行(1 => 列 , 2 => 行) : ")
        if com == '1' or com == '2' :
            break
        else : 
            print("請輸入1或2")
    
    row = array.shape[0]
    col = array.shape[1]
    
    
    
    #input row
    if com == '1' :
        print("請問要對調哪兩列")
        while(1) : 
            Change1 = int(input("請輸入列(請介於0和" + str(row-1) + "之間) : "))
            if 0 <= Change1 < row :
                break;
            else : 
                print("請介於0和" + str(row) + "之間")
                
        while(1) : 
            Change2 = int(input("請輸入列(請介於0和" + str(row-1) + "之間) : "))
            if 0 <= Change2 < row :
                break;
            else : 
                print("請介於0和" + str(row) + "之間")
    
                
    #input col
    elif com == '2' :
        print("請問要對調哪兩行")
        while(1) : 
            Change1 = int(input("請輸入列(請介於0和" + str(col-1) + "之間) : "))
            if 0 <= Change1 < col :
                break;
            else : 
                print("請介於0和" + str(col) + "之間")
        while(1) : 
            Change2 = int(input("請輸入列(請介於0和" + str(col-1) + "之間) : "))
            if 0 <= Change2 < col :
                break;
            else : 
                print("請介於0和" + str(col) + "之間")
        
    return change(array , Change1 , Change2 , com)

def change(array , change1 , change2 , com) :
    #計算行數列數
    rows , cols = array.shape
    #row
    if com == '1' :
        array[[change1,change2] , :] = array[[change2,change1] , :]
        print(array)
        print(str(change1) + "列和" + str(change2) + "列已經對調")
        
        
    #col
    elif com == '2' :
        array[: , [change1,change2]] = array[: , [change2,change1]]
        print(array)
        print(str(change1) + "行和" + str(change2) + "行已經對調")
        
    return array

#2 of function end


#3 of function
def three(array) :
    changeStr = input("請輸入要調換的字串 : ")
    changeTo = input("請輸入要換成什麼字串 : ")
    
    #計算row col
    row , col = array.shape
    
    newArray = numpy.empty([row , col], dtype = ('object'))
    
    for i in range(row) :
        for j in range(col) :
            if array[i,j] == changeStr :
                print(changeTo)
                newArray[i,j] = changeTo
            else :
                newArray[i,j] = array[i,j]
          
    str(newArray)
    print(newArray)
    print("已經將" + str(changeStr) + "換成" + str(changeTo))
    
    return newArray

#3 of function end


'''
function part end
'''



'''
main function
'''
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
        print("output")
        print(array)
    elif command == '2' :
        print("欄位調換")
        array = two(array)
        print("output")
        print(array)
    elif command == '3' :
        print("欄位處理(調換有指定字的欄位)")
        array = three(array)
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
    
'''
end of main function
'''











