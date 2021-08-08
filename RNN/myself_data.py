# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 22:57:47 2021

@author: User
"""

from __future__ import absolute_import, division, print_function, unicode_literals
import keras
import tensorflow as tf
import numpy as np
import os
import time

#資料預處理
def spilt_input_target(chunk) :
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

path_to_file = keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
#print(len(text)) 看看裡面有幾個字

vocab = sorted(set(text))
#print(len(vocab))
#print(vocab)  檢視有幾個獨特的字符

char_index = { u:i for i, u in enumerate(vocab)}
index_char = np.array(vocab)
#print(char_index)
#print(index_char)

text_as_int = np.array([char_index[c] for c in text])
#print(text_as_int)
#print(text[:5], text_as_int[:5])

seq_length = 100
example_per_epoch = len(text) // seq_length

char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)  #向量轉字符index
#for i in char_dataset.take(10) :
    #print(index_char[i.numpy()])
    
sequences = char_dataset.batch(seq_length+1, drop_remainder=True)  #計算字句
#for item in sequences.take(5) :
    #print(repr(''.join(index_char[item.numpy()])))

dataset = sequences.map(spilt_input_target)
'''
for input_example, target_example in dataset.take(1) :  #test print input and output
    print("Input data : ", repr(''.join(index_char[input_example])))
    print("Target data : ", repr(''.join(index_char[target_example])))


for i, (input_idx, target_idx) in enumerate(zip(input_example[:5], target_example[:5])):
    print("Step {:4d}".format(i))
    print("\tinput: {} ({:s})".format(input_idx, repr(index_char[input_idx])))
    print("\texpected output: {} ({:s})".format(target_idx, repr(index_char[target_idx])))    
'''

batch_size = 64
steps_per_epoch = example_per_epoch // batch_size

buffer_size = 1000
dataset = dataset.shuffle(buffer_size).batch(batch_size, drop_remainder=True)

#print(dataset)





#建立model
from keras import Sequential
from keras.layers import Embedding, RNN, Dense, LSTM, GRU

def build_model(vocab_size, emdedding_dim, rnn_units, batch_size) :
    
    model = Sequential()
    model.add(Embedding(vocab_size, embedding_dim,batch_input_shape=[batch_size, None]))
    model.add(GRU(rnn_units,return_sequences=True,recurrent_initializer='glorot_uniform',stateful=True))
    model.add(Dense(vocab_size))
    return model

def loss(labels, logits) :
    return keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

vocab_size = len(vocab)  #獨特字符的長度
embedding_dim = 256   #設定embedding的dimension
RNN_units = 1024  #設定RNN的單元數

#設置並建立model
model = build_model(vocab_size=len(vocab), emdedding_dim=embedding_dim, rnn_units=RNN_units, batch_size=batch_size)

for input_example_batch, target_example_batch in dataset.take(1):
  example_batch_predictions = model(input_example_batch)
  #print(example_batch_predictions.shape, "# (batch_size, sequence_length, vocab_size)")

model.summary()

#training model
example_batch_loss = loss(target_example_batch, example_batch_predictions)

model.compile(optimizer='adam', loss=loss)

'''
做到62行的程式
記得這個做完去將原本的改RNN交就好
不要白癡做兩個範例
'''



