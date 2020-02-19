# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
# https://drive.google.com/file/d/1BjMJSJ2VntPFiYaoYehqsx5cr69F7Hva/view?usp=sharing
num = input('Введите число: ')
b = ''
for i in num:
    b = i + b
print(int(b))