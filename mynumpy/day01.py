# -*- coding: utf-8 -*-
import numpy as np
data = np.random.randint(2, 3)
print(data)

data = np.array([1, 3, 4, 5])
print(data)
print(data.shape)

data = np.ndarray([1, 3, 4, 5])
print(data)
print(data.shape)

data = np.arange(10)
print(data)

data = data.astype(np.float64)
print(data)

data = np.array([[1, 2, 3], [2, 3, 4]])
data = data * data
print(data)
data = 1
print(data)

arr = np.empty((8,	4))
print(arr)
for i in range(8):
    arr[i] = i
print(arr)
new_arr = arr[[1, 2, 3]]
print(new_arr)
new_arr[0] = 0
print(new_arr)
print(arr)