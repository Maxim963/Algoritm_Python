# Во втором массиве сохранить индексы четных элементов первого массива.
from random import randint

size = 20
min = 0
max = 20
arr = [randint(min, max) for i in range(size)]
chet = []
for i, j in enumerate(arr):
    if j % 2 == 0:
        chet.append(i)
print(arr)
print(chet)
