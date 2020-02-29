# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

big = 0
little = 0
arr = [randint(1, 20) for i in range(15)]
print(arr)
for i in arr:
    if i > big:
        big = i
    little = big
for j in arr:
    if j < little:
        little = j
for s, e in enumerate(arr):
    if e == big:
        arr[s] = little
    elif e == little:
        arr[s] = big
print(little, big, sep=' < ')
print(arr)
