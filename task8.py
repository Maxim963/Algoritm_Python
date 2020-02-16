# Определить, является ли год, который ввел пользователь, високосным или не високосным.
# https://drive.google.com/file/d/1FTK2Dz6qM8ZuiTbD29HXaAylIxoAuAhA/view?usp=sharing

y = int(input('Введите год: '))
if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print('Год не високосный')
else:
    print('Год високосный')
