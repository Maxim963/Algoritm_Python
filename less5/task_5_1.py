# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Kvart = 4
companys = namedtuple('komp', ['name', 'kvartal', 'itogo'])
all = set()
count = input("Кол-во компаний: ")
itogo_vsego = 0
for i in range(1, (int(count) + 1)):
    name = input(f'Название компании {i}: ')
    kvartal = []
    itogo = 0
    for j in range(Kvart):
        kvartal.append(int(input(f'Прибыль за квартал {j + 1}: ')))
        itogo += kvartal[j]
    company = companys(name=name, kvartal=tuple(kvartal), itogo=itogo)
    all.add(company)
    itogo_vsego += itogo
sred = itogo_vsego / int(count)

print('Средняя прибыль = ', sred)

print('\nВыше среднего: ')
for c in all:
    if c.itogo > sred:
        print(f'Прибыль компании {c.name} = {c.itogo}')

print('\n', 'Ниже среднего: ')
for c in all:
    if c.itogo < sred:
        print(f'Прибыль компании {c.name} = {c.itogo}')
