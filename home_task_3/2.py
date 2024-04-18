arr = ['name', 'world', 'python']

max_len = 0
max_word = ''
for el in arr:
    if len(el) > max_len:
        max_len = len(el)
        max_word = el
print(max_word)

max_len = 0
max_word = ''

i = 0
while i < len(arr):
    if len(arr[i]) > max_len:
        max_len = len(arr[i])
        max_word = arr[i]
    i += 1
print(max_word)