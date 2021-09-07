# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:21:40 2021

@author: User
"""
import numpy

listtest1 = [['A','B'],['C','D'],['E','F'],['G','H']]
listtest2 = [['A','B','C','D'],['E','F','G','H']]
change = 'PPPP'

listtest1 = numpy.array(listtest1)

listtest1[0,:] += listtest1[1,:]

print(listtest1)


#listtest = [[row[i]  if i != 1 else row[1]+row[0] for i in range(len(listtest1[0])) if i != 0 ]   for row in listtest1]

'''
listtest = [
            [b for j,b in enumerate(a)] if i != 1 else
            [b+listtest1[3][j] for j,b in enumerate(a)]
            for i,a in enumerate(listtest1) if i != 3
            ]
'''
#print(listtest)


