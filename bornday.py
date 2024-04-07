year = int(input('Введите год рождения А.С.Пушкин: '))
if year != 1799:
    print('Неверный год')
elif year == 1799:
    day = int(input('Введите день рождения А.С.Пушкин: '))
if day == 6:
    print('Верно')
else:
    print('Неверный день рождения')