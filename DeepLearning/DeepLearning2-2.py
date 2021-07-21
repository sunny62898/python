# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:40:06 2021

@author: User
"""


import torch, torchvision

a = torch.tensor([2., 3.], requires_grad=True)
b = torch.tensor([6., 4.], requires_grad=True)

Q = 3*a**3 - b**2

external_grad = torch.tensor([1., 1.])
Q.backward(gradient=external_grad)

print(9*a**2 == a.grad)
print(-2*b == b.grad)


x = torch.rand(5, 5)
y = torch.rand(5, 5)
z = torch.rand((5, 5), requires_grad=True)

a = x + y
print(f"Does 'a' require gradients? : {a.requires_grad}" )
b = x + z
print(f"Does 'b' require gradients?: {b.requires_grad}")

from torch import nn, optim

model = torchvision.models.resnet18(pretrained=True)

#凍結所有參數
for param in model.parameters() :
    param.requires_grad = False

model.fc = nn.Linear(512, 10)

#現在除了model.fc的參數沒有被凍結 其他都被凍結了

optimizer = optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)

