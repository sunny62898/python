# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:23:37 2021

@author: User
"""

import torch, torchvision

model = torchvision.models.resnet18(pretrained=True)
data = torch.rand(1, 3, 64, 64)
labels = torch.rand(1, 1000)

#forward pass
prediction = model(data)

loss = (prediction - labels).sum()
loss.backward()  #backward pass

#設置一個SGD模板
optim = torch.optim.SGD(model.parameters(), lr = 1e-2, momentum=0.9)

optim.step()  #梯度下降
print(optim)



