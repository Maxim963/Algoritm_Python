# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]
from collections import deque

standart = 16
num1 = ('0', '1', '2', '3', '4',
        '5', '6', '7', '8', '9',
        'A', 'B', 'C', 'D', 'E', 'F')

num2 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def sum(per, vtor):
    per = per.copy()
    vtor = vtor.copy()
    if len(per) < len(vtor):
        per, vtor = vtor, per
    vtor.extendleft('0' * (len(per) - len(vtor)))
    zapas = 0
    ravno = deque()
    while len(per) != 0:
        per_ch = num2[per.pop()]
        vtor_ch = num2[vtor.pop()]
        ravno_ch = per_ch + vtor_ch + zapas
        if ravno_ch >= standart:
            zapas = 1
            ravno_ch -= standart
        else:
            zapas = 0
        ravno.appendleft(num1[ravno_ch])
    if zapas == 1:
        ravno.appendleft('1')
    return ravno


def umn(per, vtor):
    per = per.copy()
    vtor = vtor.copy()
    if len(per) < len(vtor):
        per, vtor = vtor, per
    vtor.extendleft('0' * (len(per) - len(vtor)))
    ravno = deque('0')
    while len(vtor) != 0:
        vtor_ch = num2[vtor.pop()]
        sp = deque('0')
        for _ in range(vtor_ch):
            sp = sum(sp, per)
        sp.extend('0' * (len(per) - len(vtor) - 1))
        ravno = sum(ravno, sp)
    return ravno


a = input('Первое число: ')
b = input('Второе число: ')

a1 = deque(a.upper())
b1 = deque(b.upper())
print(f'{list(a1)} + {list(b1)} = {list(sum(a1, b1))}')
print(f'{list(a1)} * {list(b1)} = {list(umn(a1, b1))}')
