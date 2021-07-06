# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:54:39 2021

@author: User
"""

#input
'''
    在input的指令中
    所輸入的都換被轉換成string
    如果要轉換成其他的資料型態
    那就 int(input('Enter number')) 來轉換
'''
name = input("Enter name : ")
print(name)

#number = input("Enter number : ")  會自動將輸入變成string
number = int(input("Enter number : "))
print(number + 3)


'''
    在python裡區塊是用tab表示
    (同一個tab之間的都是同一個區塊)
    所以不需要{}來括起來
'''
#if
dic1 = "aza"
dic2 = "741"
account = input("Enter account : ")

if account == dic1 :
    print("correct")
elif account == dic2 :
    print("correct")
else : 
    print("error")
    print("77777")
print("789789789")  #扣掉tab => 一定會執行 不算在if else裡


#while
add = 0
while add < 10 :
    print(add , end = '')  #後面加上end = ''可以印出不換行
    add = add +1

print("fin")

#for
array = ["kk","pp","ee"]
for i in range(0,len(array)) :
    print(array[i])

for n in array : 
    print(n)
    
#exercise
n = int(input("Enter a number : "))

for i in range(0,n) : 
    for j in range(0,n-i) : 
        print(" ",end = '')
    for k in range(0,i*2+1):
        print("*",end = '')
    print()

for i in range(0,n) :
    for j in range(0,n) : 
        print(" ",end = '')
    print("*")

