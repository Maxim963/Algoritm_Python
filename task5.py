# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# https://drive.google.com/file/d/1FTK2Dz6qM8ZuiTbD29HXaAylIxoAuAhA/view?usp=sharing

print('Введите две буквы')
a = input('первая буква: ')
b = input('вторая буква: ')
c = ord(a) - ord('a') + 1
d = ord(b) - ord('a') + 1
mej = int()
if c < d:
    mej = d - c - 1
    print(f'Между %s и %s - %d букв' % (a, b, mej))
elif c > d:
    mej = c - d - 1
    print(f'Между %s и %s - %d букв' % (a, b, mej))
else:
    print('Две одинаковые буквы')
print(f'Порядковый номер буквы %s = %d' % (a, c))
print(f'Порядковый номер буквы %s = %d' % (b, d))
