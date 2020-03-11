# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint
import timeit, cProfile

arr = [randint(1, 20) for i in range(125000)]
arr1 = [randint(1, 20) for i in range(250000)]
arr2 = [randint(1, 20) for i in range(500000)]
arr3 = [randint(1, 20) for i in range(1000000)]


# print(arr)
def minmax(ttt):
    big = 0
    little = 0
    for i in ttt:
        if i > big:
            big = i
        little = big
    for j in ttt:
        if j < little:
            little = j
    for s, e in enumerate(ttt):
        if e == big:
            ttt[s] = little
        elif e == little:
            ttt[s] = big
    return ttt


# print(little, big, sep=' < ')
print(timeit.timeit('minmax(arr)', number=200, globals=globals()))  # 3.0654204
print(timeit.timeit('minmax(arr1)', number=200, globals=globals()))  # 6.122196500000001
print(timeit.timeit('minmax(arr2)', number=200, globals=globals()))  # 12.2651746
print(timeit.timeit('minmax(arr3)', number=200, globals=globals()))  # 24.4739928

cProfile.run('minmax(arr)')  # 4 function calls in 0.015 seconds
cProfile.run('minmax(arr1)')  # 4 function calls in 0.030 seconds
cProfile.run('minmax(arr2)')  # 4 function calls in 0.061 seconds
cProfile.run('minmax(arr3)')  # 4 function calls in 0.122 seconds
