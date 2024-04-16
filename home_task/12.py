s = '1, 2, 3'
arr = list(map(int, s.split(', ')))
print(arr)

tup = tuple(map(int, s.split(', ')))
print(tup)