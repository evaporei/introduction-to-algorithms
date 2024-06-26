l = [3, 8, 4, 5, 2, 10, 1, 3]

# # works, first version, sloppy
# for i in range(len(l)):
#     min_val = l[i]
#     j = i + 1
#     idx = None
#     while j < len(l):
#         if min_val > l[j]:
#             min_val = l[j]
#             idx = j
#         j += 1
#     if idx:
#         l[idx] = l[i]
#         l[i] = min_val

# works, cleaner
for i in range(len(l)):
    min_idx = i
    for j in range(i + 1, len(l)):
        if l[j] < l[min_idx]:
            min_idx = j
    l[i], l[min_idx] = l[min_idx], l[i]

print(l)
