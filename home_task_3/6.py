number = input()
#print(len(number))
count = 0
for el in number:
    if el.isdigit():
        count += 1
print(f'Количество цифр в числе: {count}')


count = 0
number = int(number)
while number != 0:
    count += 1
    number //= 10
print(f'Количество цифр в числе: {count}')