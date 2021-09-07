# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 22:02:36 2021

@author: User
"""


from scipy import stats
import numpy as np


#sample size
N = 10

a = np.random.randn(N) + 2
b = np.random.randn(N)

var_a = a.var(ddof=1)
var_b = b.var(ddof=1)

#std deviation
s = np.sqrt((var_a+var_b)/2)

#統計量
t = (a.mean() - b.mean())/(s*np.sqrt(2/N))

#自由度
df = 2*N - 2

#計算p-value after comparison with the t
p = 1 - stats.t.cdf(t,df=df)

print("t = " + str(t))
print("p = " + str(2*p))  #p為兩倍是因為是兩邊的t-tail所組成

#交叉參照
t2, p2 = stats.ttest_ind(a, b)

print("t2 = " + str(t2))
print("p2 = " + str(p2*2))


