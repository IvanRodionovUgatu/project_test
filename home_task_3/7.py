s = input()
s_reverse = ''
for i in range(len(s) - 1, -1, -1):
    s_reverse += s[i]
if s == s_reverse:
    print('Палиндромом')
else:
    print('Не палиндромом')