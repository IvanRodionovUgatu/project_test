print('Пн Вт Ср Чт Пт Сб Вс')
for i in range(1, 31 + 1):
    if i < 10:
        print(i, end='  ')
    else:
        print(i, end=' ')
    if i % 7 == 0:
        print()