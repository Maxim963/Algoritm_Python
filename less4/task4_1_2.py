# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint
import timeit, cProfile

arr = [randint(1, 20) for i in range(125000)]
arr1 = [randint(1, 20) for i in range(250000)]
arr2 = [randint(1, 20) for i in range(500000)]
arr3 = [randint(1, 20) for i in range(1000000)]


# print(arr)
def minmax(ttt):
    little = 0
    big = 0
    for i in range(len(ttt)):
        if ttt[i] < ttt[little]:
            little = i
        elif ttt[i] > ttt[big]:
            big = i
    ttt[little], ttt[big] = ttt[big], ttt[little]
    return ttt


print(timeit.timeit('minmax(arr)', number=200, globals=globals()))  # 2.4987816
print(timeit.timeit('minmax(arr1)', number=200, globals=globals()))  # 4.9852589
print(timeit.timeit('minmax(arr2)', number=200, globals=globals()))  # 9.897634600000002
print(timeit.timeit('minmax(arr3)', number=200, globals=globals()))  # 19.961045400000003

cProfile.run('minmax(arr)')  # 5 function calls in 0.012 seconds
cProfile.run('minmax(arr1)')  # 5 function calls in 0.024 seconds
cProfile.run('minmax(arr2)')  # 5 function calls in 0.050 seconds
cProfile.run('minmax(arr3)')  # 5 function calls in 0.098 seconds
