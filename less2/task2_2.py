# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://drive.google.com/file/d/1BjMJSJ2VntPFiYaoYehqsx5cr69F7Hva/view?usp=sharing
num = input('Введите число: ')
a = ''
b = ''
for i in num:
    if int(i) % 2 == 0:
        a += i
    else:
        b += i
print(f'Чет-е - {a} %d шт. \nНечет-е - {b} %d шт.' % (len(a), len(b)))
