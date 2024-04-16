arr = [1, 2, 3, 3, 4, 5, 5]
if len(arr) == len(set(arr)):
    print('Все уникальны')
else:
    print('Есть дубликаты')