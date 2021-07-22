# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:21:40 2021

@author: User
"""

listtest1 = [['A','B','C','D'],['E','F','G','H']]
listtest2 = [['A','B','C','D'],['E','F','G','H']]
change = 'PPPP'


#listtest = [[row[i]  if i != 2 else row[2]+row[0] for i in range(len(listtest1[0])) if i != 0 ]   for row in listtest1]
print(listtest1[0][0])
listtest = [if i != 0 else listtest1[i] for i in range(len(listtest))]


