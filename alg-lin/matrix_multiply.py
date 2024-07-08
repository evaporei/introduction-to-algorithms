def matrix_multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    c = [[0 for _ in range(len(a))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                c[i][j] += a[i][k] * b[k][j]
    return c

# swap j and k muahaha (better cache utilization)
def faster(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    c = [[0 for _ in range(len(a))] for _ in range(len(a))]
    for i in range(len(a)):
        for k in range(len(a)):
            for j in range(len(a)):
                c[i][j] += a[i][k] * b[k][j]
    return c

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# [[30, 24, 18],
#  [84, 69, 54],
#  [138, 114, 90]]
print(matrix_multiply(a, b))
print(faster(a, b))
