arr = [3, 8, 2, 9, 2, 3, 4, 5, 10, 1]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)
