import timeit, cProfile


def prosto(x):
    n = 10000
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst[x - 1]


print(timeit.timeit('prosto(500)', number=100, globals=globals()))  # 0.440691
cProfile.run('prosto(500)')  # 1232 function calls in 0.005 seconds

# print(prosto(500))
