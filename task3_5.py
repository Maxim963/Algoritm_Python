# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
from random import randint

size = 20
min = -20
max = 10
arr = [randint(min, max) for i in range(size)]
low = []
big = 0
ind = set()
for i in arr:
    if i < 0:
        low.append(i)
big = low[0]
for i in low:
    for b in low:
        if i > b and i > big:
            big = i
for i, j in enumerate(arr):
    if j == big:
        ind.add(i)
print(f' {big }, индекс(ы) {ind}')
print(arr)
