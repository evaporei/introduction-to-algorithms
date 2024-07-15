class Heap:
    items: list[int]

    # it will modify items in place!
    def __init__(self, items: list[int]):
        # I don't like this, but it's necessary
        # to implement heapsort
        self.length = len(items)

        self.items = items
        self.build_heap()

    def build_heap(self):
        for i in reversed(range(self.length // 2)):
            self.heapify(i)

    def heapify(self, i: int):
        l, r = self.left(i), self.right(i)
        largest = i

        if l < self.length and self.items[l] > self.items[i]:
            largest = l

        if r < self.length and self.items[r] > self.items[largest]:
            largest = r

        if largest != i:
            self.items[i], self.items[largest] = self.items[largest], self.items[i]
            self.heapify(largest)

    def left(self, i: int) -> int:
        return 2 * i + 1

    def right(self, i: int) -> int:
        return 2 * i + 2

    def peek(self) -> int:
        return self.items[0]

    def pop(self) -> int:
        self.items[0], self.items[-1] = self.items[-1], self.items[0]
        max_val = self.items.pop()
        self.length -= 1
        self.heapify(0)
        return max_val
    
    def size(self) -> int:
        return self.length

    # breaks heap order, but returns sorted list
    def sort(self) -> list[int]:
        original_length = self.length
        for i in reversed(range(1, self.length)):
            self.items[0], self.items[i] = self.items[i], self.items[0]
            self.length -= 1
            self.heapify(0)
        self.length = original_length
        return self.items


heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(heap.items)
print(heap.pop())
print(heap.items)
print(heap.sort())
