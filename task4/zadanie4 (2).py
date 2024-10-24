# -*- coding: utf-8 -*-
"""Zadanie4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hid4Ru1YndfJGVWfuSfW3je3m1abQhmC
"""

import numpy as np
import matplotlib.pyplot as plt

n = 41
h = 5
N = (n - 2) ** 2

def idx(i, j):
    return (i - 1) * (n - 2) + (j - 1)

A = np.zeros((N, N))
b = np.zeros(N)

left = np.linspace(150, 50, n)
right = np.linspace(200, 50, n)
top = np.full(n, 100)
bottom = np.full(n, 100)

for i in range(1, n-1):
    for j in range(1, n-1):
        index = idx(i, j)
        A[index, index] = -4
        if i == 1:
            b[index] -= left[j]
        else:
            A[index, idx(i-1, j)] = 1

        if i == n-2:
            b[index] -= right[j]
        else:
            A[index, idx(i+1, j)] = 1

        if j == 1:
            b[index] -= top[i]
        else:
            A[index, idx(i, j-1)] = 1

        if j == n-2:
            b[index] -= bottom[i]
        else:
            A[index, idx(i, j+1)] = 1

T = np.linalg.solve(A, b)

T_2d = np.zeros((n, n))
T_2d[0, :] = top
T_2d[-1, :] = bottom
T_2d[:, 0] = left
T_2d[:, -1] = right
for i in range(1, n-1):
    for j in range(1, n-1):
        T_2d[i, j] = T[idx(i, j)]

plt.imshow(T_2d, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Rozkład temperatury na płytce')
plt.show()