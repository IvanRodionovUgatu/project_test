arr = [1, 2, 3, 5, 5, 1, 5, 8, 9]
arr.sort()
print(arr)

i = 0
while i < len(arr) - 1:
    if arr[i] == arr[i + 1]:
        del arr[i]
        i -= 1
    i += 1

print(arr)
