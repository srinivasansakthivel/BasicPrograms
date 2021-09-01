n = int(input("Enter the number of rows : "))

for row in range(n):
    k = 1
    for col in range(n - row):
        print(k, end=" ")
        k += 1
    print() 

# for row in range(n):
#     for col in range(n - row):
#         print(n-row, end=" ")
#     print()


