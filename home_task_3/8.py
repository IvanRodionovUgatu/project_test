arr = [1, 2, 3, 3]
flag = False

for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1]:
        print('Есть дубликаты')
        flag = True
        break
if not flag:
    print('Дубликатов нет')

