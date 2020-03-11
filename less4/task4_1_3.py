# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint
import timeit, cProfile

arr = [randint(1, 20) for i in range(125000)]
arr1 = [randint(1, 20) for i in range(250000)]
arr2 = [randint(1, 20) for i in range(500000)]
arr3 = [randint(1, 20) for i in range(1000000)]


# print(arr)
def minmax(ttt):
    little_num = min(ttt)
    big_num = max(ttt)
    little = ttt.index(little_num)
    big = ttt.index(big_num)
    ttt[little], ttt[big] = ttt[big], ttt[little]
    return ttt


print(timeit.timeit('minmax(arr)', number=200, globals=globals()))  # 0.48502350000000005
print(timeit.timeit('minmax(arr1)', number=200, globals=globals()))  # 0.9694902999999999
print(timeit.timeit('minmax(arr2)', number=200, globals=globals()))  # 1.9350063999999998
print(timeit.timeit('minmax(arr3)', number=200, globals=globals()))  # 3.8724070999999993

cProfile.run('minmax(arr)')  # 8 function calls in 0.002 seconds
cProfile.run('minmax(arr1)')  # 8 function calls in 0.005 seconds
cProfile.run('minmax(arr2)')  # 8 function calls in 0.010 seconds
cProfile.run('minmax(arr3)')  # 8 function calls in 0.020 seconds
