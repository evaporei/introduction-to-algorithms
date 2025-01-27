# example:
# [16, 14, 10, 4, 7, 9, 3]
#
# tree viz:
#     16    
#   14   10  
# 4   7 9  3 
#
# idxs:
#       0
#    1     2
#  3  4  5   6

# parent(3) -> 2 // 2 -> 1
# parent(4) -> 3 // 2 -> 1
def parent(i: int) -> int:
    return (i - 1) // 2

# left(1) -> 2 + 1 -> 3
# left(2) -> 4 + 1 -> 5
def left(i: int) -> int:
    return 2 * i + 1

# right(1) -> 2 + 2 -> 4
# right(2) -> 4 + 2 -> 6
def right(i: int) -> int:
    return 2 * i + 2

# length was added to support heapsort
# and because we have no new class in this file
def heapify(heap: list[int], i: int, length: int):
    l, r = left(i), right(i)
    largest = i

    if l < length and heap[l] > heap[i]:
        largest = l

    if r < length and heap[r] > heap[largest]:
        largest = r

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(heap, largest, length)

def build_heap(xs: list[int]):
    for i in reversed(range(len(xs) // 2)):
        heapify(xs, i, len(xs))

def heap_max(heap: list[int]) -> int:
    return heap[0]

def heap_pop(heap: list[int]) -> int:
    heap[0], heap[-1] = heap[-1], heap[0]
    max_val = heap.pop()
    heapify(heap, 0, len(heap))
    return max_val

# breaks heap property, you'll need to heapify again
def heap_sort(heap: list[int]):
    length = len(heap)
    for i in reversed(range(1, len(heap))):
        heap[0], heap[i] = heap[i], heap[0]
        length -= 1
        heapify(heap, 0, length)


heap = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]

print(heap)

build_heap(heap)

# [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0]
#            27
#      17          10
#   16    13     9    1
# 5   7 12  4  8  3  0
print(heap)

heap2 = [3, 4, 7, 9, 10, 14, 16]
build_heap(heap2)
# [16, 10, 14, 9, 4, 3, 7]
print(heap2)

print(heap_pop(heap2))
print(heap2)

heap_sort(heap2)
# regular sorted list
print(heap2)
