list1 = [56, 5, 10, 23, 46, 10]
print("Unsorted List", list1)

for i in range(len(list1)-1):
    min_val = min(list1[i:])
    min_ind = list1.index(min_val, i)
    if list[i] != list1[min_ind]:
        list1[i], list1[min_ind] = list1[min_ind], list1[i]
print(list1)