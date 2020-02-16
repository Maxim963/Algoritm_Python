# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# https://drive.google.com/file/d/1FTK2Dz6qM8ZuiTbD29HXaAylIxoAuAhA/view?usp=sharing

print('Введите 3 числа')
a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))
if a < b < c or c < b < a:
    print(f'Среднее {b}')
elif b < a < c or c < a < b:
    print(f'Среднее {a}')
elif b < c < a or a < c < b:
    print(f'Среднее {c}')
else:
    print('Введены повторяющиеся цифры')
