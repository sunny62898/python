# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 01:01:37 2021

@author: User
"""

#list
"""
    list
    可以包含不同的資料型態
    (但最好是相同型態不然跟tuple一樣)
    但是如果要排序或需要相同資料型態的事情
    那就會產生錯誤
    但資料型態之後依然可以更改
"""
#a = [1023,456,789,"OPP"]  這個當要排序就會錯因為有str
#a = [1023,456,789,[12,45,78]]  這個在排序也會錯因為有list
a = [1023,456,789]
print(a)

a.sort()
a.reverse()
a.insert(2, 45)
a.extend([12,7,6])
print(a)

a.pop(5)
print(a)
print(a.index(789))
print(type(a))


#tuple
"""
    tuple
    基本上list可以用的指令在tuple都很難使用
    因為他主要用在儲存各種不同型態
    因此一旦決定了型態就無法改變
    也不能用指令輕易刪除某一個index
"""
b = ("aaa",45,999,[45,66])
print(b)
print(type(b))



#dictionary
"""
    dictionary
    宣告的形式為{keys : value}  (有點類似HashMap)
    所以尋找裡面的內容會使用key值來尋找
"""
c = {45 : "PPP" , 9 : "pl" , "789" : "OO" , "aa" : 123}
print(c)
print(c.get(45))
d = c.copy()
print(d)
d.pop("789")
print('d = ' + str(d))   #利用str()將不是string的東西轉成string
c.clear()
print(c)


#range
r = range(0,9,3)   #0開始 9結束 間隔3
print(r[0],r[1],r[2])


