def insertion_sort_book(l: list[int]):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j > -1 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


def insertion_sort_book_inv(l: list[int]):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j > -1 and l[j] < key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


def insertion_sort_net(l: list[int]):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1

def insertion_sort_net_inv(l: list[int]):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j] > l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1

def search(l: list[int], n: int) -> int:
    for i in range(len(l)):
        if l[i] == n:
            return i
    return -1

nums = [3, 5, 2, 9, 8, 2, 10, 3]
print(nums)
insertion_sort_book(nums)
print(nums)
insertion_sort_book_inv(nums)
print(nums)
insertion_sort_net(nums)
print(nums)
insertion_sort_net_inv(nums)
print(nums)

print(search(nums, 9))
