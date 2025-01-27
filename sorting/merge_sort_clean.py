def merge(xs: list[int], p: int, q: int, r: int):
    left = xs[p:q+1]
    right = xs[q+1:r+1]

    i = j = 0
    k = p
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            xs[k] = left[i]
            i += 1
        else:
            xs[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        xs[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        xs[k] = right[j]
        j += 1
        k += 1

def sort(xs: list[int], p: int, r: int):
    if p >= r:
        return
    q = (p + r) // 2
    sort(xs, p, q)
    sort(xs, q + 1, r)
    merge(xs, p, q, r)

def merge_sort(xs: list[int]):
    sort(xs, 0, len(xs) - 1)

arr = [4, 3, 2, 1]
print(arr)
merge_sort(arr)
print(arr)

print()

arr = [3, 8, 2, 5, 4, 9, 10, 2, 3]
print(arr)
merge_sort(arr)
print(arr)
