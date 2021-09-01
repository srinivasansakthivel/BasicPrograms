num = int(input("Enter a positive integer number : "))
result = 0
while num > 0:
    digit = num % 10
    result = result + digit
    num = num // 10

print("Sum of the positive integer is : ", result)