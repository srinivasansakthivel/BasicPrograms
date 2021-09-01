num = int(input("Enter the number greater than 1 to check whether it is perfect or Not : "))
summation = 0
if num > 1:
    for i in range(1, num):
        if num % i == 0:
            summation = summation + i
if summation == num:
    print(num, " is a prefect number")
else:
    print(num, "is not a perfect number")