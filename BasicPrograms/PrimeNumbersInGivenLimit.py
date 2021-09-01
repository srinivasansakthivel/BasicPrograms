lower = int(input("Enter the lower limit value : "))
upper = int(input("Enter the upper limit value : "))
for num in range(lower, upper+1):
    if num > 1:
        for divisor in range(2, num):
            if num % divisor == 0:
                break
        else:
            print(num, end=" ")
