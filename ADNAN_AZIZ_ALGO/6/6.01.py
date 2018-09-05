import random
import numpy as np
import matplotlib.pyplot as plt

def swaptill(l, i, j):
    idx = j
    while (idx > i):
        l[idx], l[idx-1] = l[idx-1],l[idx]
        idx -= 1
    return l

def partition(l, pivot_idx):
    j = 1
    k = 1
    pivot = l[pivot_idx]
    l[pivot_idx], l[0] = l[0], l[pivot_idx]

    for i in range(1,len(l)):
        if pivot == l[i]:
            l = swaptill(l, k-1, i)
            k += 1

        if pivot > l[i]:
            l = swaptill(l, j-1, i)
            j += 1
            k += 1

        if pivot < l[i]:
            print('greater')
    return l

def partition_better(l, pivot_idx):
    j = 0
    k = 1
    pivot = l[pivot_idx]
    l[pivot_idx], l[0] = l[0], l[pivot_idx]

    for i in range(1,len(l)):
        if pivot == l[i]:
            l[k], l[i] = l[i],l[k]
            k += 1

        if pivot > l[i]:
            l[k], l[i] = l[i], l[k]
            l[k], l[j] = l[j], l[k]
            j += 1
            k += 1

    return l

t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = [2, 1, 0, 0, 1, 2, 2, 1, 0]

print(partition_better(list(reversed(t)), 4))