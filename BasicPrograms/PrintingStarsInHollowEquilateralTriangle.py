n = int(input("Enter the number of rows: "))
for row in range(1, n+1):
    for col in range(1, 2*n):
        if row+col == n+1 or col-row == n-1 or row == n:
            print("*",end="")
        else:
            print(end=" ")
    print()