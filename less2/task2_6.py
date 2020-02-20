# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ.
# https://drive.google.com/file/d/1BjMJSJ2VntPFiYaoYehqsx5cr69F7Hva/view?usp=sharing
from random import *
x = randint(0, 100)
count = 0
while True:
    if count == 10:
        print(f'Это число {x}')
        break
    y = int(input('угадайте число до 100:  '))
    if y < x:
        count += 1
        print(' Больше...')
    elif y > x:
        count += 1
        print('Меньше...')
    else:
        print('\n', 'Угадано это',  x, '\n',  'за', + count,  'попыток', '\n', '\n')
        break


