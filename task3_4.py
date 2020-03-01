# Определить, какое число в массиве встречается чаще всего
from random import randint


def reapeat(a_list: list) -> tuple:
    max_tuple = (0, a_list[0])  # Кортеж (сколько раз встречается, какое число)
    for i in a_list:
        count = a_list.count(i)
        if count > max_tuple[0]:
            max_tuple = (count, i)
    return max_tuple


arr = [randint(1, 10) for i in range(30)]
counts = reapeat(arr)
print(arr)
print(f'Чаще всех повторяется {counts[1]}, число повторяется {counts[0]} раз(а)')
