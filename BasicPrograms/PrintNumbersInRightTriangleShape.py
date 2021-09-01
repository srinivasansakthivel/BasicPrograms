n = int(input("Enter the number of rows : "))
k = 1
for row in range(1, n+1):
    for col in range(1, row+1):
        print(k,end=" ")
        k += 1
    print()