l = [3, 8, 2, 5, 4, 9, 10, 2, 3]

# haskell wannabe:
def merge_hs(xs: list[int], ys: list[int]) -> list[int]:
    if len(xs) == 0:
        return ys
    if len(ys) == 0:
        return xs
    x, y = xs[0], ys[0]
    xs, ys = xs[1:], ys[1:]
    if x < y:
        return [x] + merge_hs(xs, [y] + ys)
    return [y] + merge_hs([x] + xs, ys)

def merge_sort_hs(xs: list[int]) -> list[int]:
    if len(xs) == 0:
        return []
    if len(xs) == 1:
        return [xs[0]]
    q = len(xs) // 2
    left = xs[:q]
    right = xs[q:]
    return merge_hs(merge_sort_hs(left), merge_sort_hs(right))

# creates a copy
print(merge_sort_hs(l))

# book
def merge_book(xs: list[int], p: int, q: int, r: int):
    print('merge call p:', p, ' q:', q, ' r:', r)
    n_left = q - p + 1
    n_right = r - q

    # make copies
    left = [xs[p + i] for i in range(n_left)]
    # or
    left = xs[p:q+1]
    print('left copy', left)

    right = [xs[q + j + 1] for j in range(n_right)]
    # or
    right = xs[q+1:r+1]
    print('right copy', right)

    i = j = 0
    k = p
    # while i < n_left and j < n_right:
    # # or
    while i < len(left) and j < len(right):
        print('while')
        if left[i] <= right[j]:
            print('left <= right', i, j)
            xs[k] = left[i]
            i += 1
        else:
            print('left > right', i, j)
            xs[k] = right[j]
            j += 1
        k += 1

    # if one is out of bounds, complete the other

    while i < n_left:
        print('while left')
        xs[k] = left[i]
        i += 1
        k += 1

    while i < n_right:
        print('while right')
        xs[k] = right[j]
        j += 1
        k += 1
    print('new range p', p, 'to k', k, ':', xs[p:k])
    print()

def merge_sort_book(xs: list[int], p: int, r: int):
    if p >= r:
        return
    print('sort call, p:', p, ' r:', r)
    q = (p + r) // 2
    merge_sort_book(xs, p, q)
    merge_sort_book(xs, q + 1, r)
    merge_book(xs, p, q, r)

# # for debugging
# l = [4, 3, 2, 1]

# in place
merge_sort_book(l, 0, len(l) - 1)

print(l)
