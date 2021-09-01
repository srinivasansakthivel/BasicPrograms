list1 = [5, 16, 20, 3, 7, 9]
print("Unsorted List", list1)

for i in range(len(list1)):
    min_val = min(list1[i:])
    min_ind = list1.index(min_val)
    list1[i], list1[min_ind] = list1[min_ind], list1[i]

print("Sorted List", list1)
