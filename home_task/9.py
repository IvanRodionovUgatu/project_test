arr1 = [1, 4, 5, 6]
arr2 = [2, 3, 6, 5]
arr = arr1 + arr2
arr.sort()
arr = list(set(arr))
print(arr)
