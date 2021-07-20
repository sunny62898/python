# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 14:23:20 2021

@author: User
"""

import torch
import numpy as np

data = [[1,2],[3,4]]
x_data = torch.tensor(data)   #宣告張量跟data一樣的torch
print(f"{data}")
print(x_data)

np_array = np.array(data)  #建立一個跟data一樣的ndarray
x_np = torch.from_numpy(np_array)   #將ndarray轉成torch型態

print(x_np)

x_ones = torch.ones_like(x_data)
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype = torch.float)
print(f"Random Tensor: \n {x_rand} \n")

shape = (2,3,)
rand_tensor = torch.rand(shape)
print(f"Random Tensor: \n {rand_tensor} \n")

ones_tensor = torch.ones(shape)
print(f"Ones Tensor: \n {ones_tensor} \n")

zeros_tensor = torch.zeros(shape)
print(f"Zeros Tensor: \n {zeros_tensor} \n")

tensor = torch.rand(3,4)
print(tensor)
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

#這裡轉換CPU到GPU的概念不懂
if torch.cuda.is_available():
    tensor = tensor.to('cuda')

print(f"Device tensor move to stored on: {tensor.device}")
#end

tensor = torch.ones(4,4)
tensor[:,1] = 0  #將第1行換成0
print(tensor)

tensor[1,:] = 0  #將第1列換成0
print(tensor)

t1 = torch.cat([tensor, tensor, tensor], dim = 1)  #橫的接起來
print(t1)

#乘法
#對應位置的矩陣相乘  所以兩個的維度要相同
print(f"tensor.mul(tensor) \n {tensor.mul(tensor)} \n")
#矩陣乘一個數值
print(f"tensor * tensor \n {tensor * tensor}")

#計算兩個矩陣相乘
print(f"tensor.T \n {tensor.T}")
print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")

print(f"tensor @ tensor.T \n {tensor @ tensor.T}")


print(x_data.T)  #.T 轉置矩陣

print(tensor , "\n")
tensor.add_(5)
print(tensor)


#tensor 轉成 numpy
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

t.add_(5)  #當原本的tensor加上數字時numpy也會跟著變動
print(f"t: {t}")
print(f"n: {n}")

#numpy array 轉成 tensor
n2 = np.ones(5)
t2 = torch.from_numpy(n2)
print(f"n2: {n2}")
print(f"t2: {t2}")

np.add(n2, 1, out = n2)  #np.add(要被加的, 加多少, 加完存到哪個變數)
print(f"n2: {n2}")
print(f"t2: {t2}")  #當numpy array被加tensor也會跟著被更動




