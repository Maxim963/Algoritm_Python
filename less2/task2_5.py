#5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
# https://drive.google.com/file/d/1BjMJSJ2VntPFiYaoYehqsx5cr69F7Hva/view?usp=sharing
for i in range(32, 128):
    print("(%4d - %s)" % (i, chr(i)), end='|')
    if i % 10 == 0:
        print()

