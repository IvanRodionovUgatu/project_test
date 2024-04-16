s = 'x'
print((s * 2).upper())
for i in range(2, 11, 2):
    res = s.upper() + s * i + s.upper()
    print(res)
