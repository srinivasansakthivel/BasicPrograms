num = int(input("Enter the number of Rows : "))
for row in range(num):
    for col in range(num):
        if row+col == 2 or row+col == 6 or col-row == 2 or row-col ==2:
            print("*", end=" ")
        else:
            print(end=" ")
    print()