# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1FTK2Dz6qM8ZuiTbD29HXaAylIxoAuAhA/view?usp=sharing
while True:
    try:
        abc = int(input('Введите трехзначное число: '))
        if len(str(abc)) != 3:
            raise ValueError
        c = abc % 100 % 10
        b = abc // 10 % 10
        a = abc // 100
        print(f'Сумма цифр числа %d = {b + c + a}' % abc)
        print(f'Произведение цифр числа %d = {b * c * a}' % abc)
    except (ValueError):
        print(f'число %d не трехзначное!' % abc)

