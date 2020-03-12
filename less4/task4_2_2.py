import timeit, cProfile


def prosto(x):
    n = 10000
    lst = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    # print(lst)
    return lst[x - 1]


print(timeit.timeit('prosto(500)', number=100, globals=globals()))  # 31.9426537
cProfile.run('prosto(500)')  # 1233 function calls in 0.324 seconds

# print(prosto(500))
