# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 17:12:05 2021

@author: User
"""
from __future__ import print_function
from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import keras
import numpy as np
import random
import sys
import io


#讀取數據
path = get_file('nietzsche.txt', origin='https://s3.amazonaws.com/text-datasets/nietzsche.txt')
with io.open(path, encoding='utf-8') as fp :
    text = fp.read().lower()
    
print("length : ", len(text))

#計算不同的字元數
chars = sorted(list(set(text)))
print("total chars : ", len(chars))

#進行one-hot code 編碼 來形成(sequences, maxlen, uni_chars)的numpy array
#提出60個chars組出一個sequence
maxlen = 60

#每三個chars採樣組成新的序列
step = 3

#保存所提出的字句
sentences = []

#保存目標(下一個char)
next_chars = []

for i in range(0, len(text) - maxlen, step) :
    #[0,59]
    sentences.append(text[i : i+maxlen])
    #[60]
    next_chars.append(text[i + maxlen])
    
print("Number of sequences : ", len(sentences))


#形成字典 每個char都對應的index
char_indict = dict((char, chars.index(char)) for char in chars)

#將one-hot編碼完的char轉成二進位的 x=三維 y=二維 之numpy array
x = np.zeros((len(sentences), maxlen, len(chars)), dtype=bool)
y = np.zeros((len(sentences), len(chars)), dtype=bool)

for i, sentence in enumerate(sentences) :
    for j, char in enumerate(sentence) :
        x[i, j, char_indict[char]] = 1
        
    y[i, char_indict[next_chars[i]]] = 1
    
#建立model
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars), activation='softmax'))
optimizer = RMSprop(lr=0.01)
model.compile(optimizer=optimizer, loss='categorical_crossentropy')
model.summary()

#給定模型預測 採樣下一個char的函數
def sample(predicts, temperature) :
    predicts = np.asarray(predicts).astype('float64')
    predicts = np.log(predicts) / temperature
    exp_preds = np.exp(predicts)
    predicts = exp_preds / np.sum(exp_preds)
    #第一個參數就是number of experiments
    problas = np.random.multinomial(1, predicts, 1)
    
    return np.argmax(problas)

#文本生成的循環(利用for來循環生成文本)
for epoch in range(1, 5) :
    print("EPOCH : ", epoch)  #訓練到第幾次
    
    #訓練model
    model.fit(x, y, batch_size=128, epochs=1)
    
    #隨機選擇文本種子
    start_index = random.randint(0, len(text) - maxlen - 1)
    generate_text = text[start_index : start_index+maxlen]
    print('---Generating with seed "' + generate_text + '"')
    
    #嘗試用不同溫度做採樣
    for temperature in [0.2, 0.5, 1.0, 1.2] :
        print("temperature : ", temperature)
        sys.stdout.write(generate_text)
        
        #從種子文本開始生成400個字
        for i in range(400) :
            #對目前生成的字進行one-hot編碼
            sampled = np.zeros((1, maxlen, len(chars)))
            
            for j, char in enumerate(generate_text) :
                sampled[0, j, char_indict[char]] = 1
                
            #對下一個字進行採樣
            preds =model.predict(sampled, verbose=0)[0]
            next_index = sample(preds, temperature)
            next_char = chars[next_index]
            generate_text += next_char
            generate_text = generate_text[1:]
            
            sys.stdout.write(next_char)
            sys.stdout.flush()
            
        print()
        

