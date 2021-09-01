import math

num = int(input("Enter the number to find the factorial : "))
if num >= 0:
    result = math.factorial(num)
    print(f'Factorial of {num} is {result}')
else:
    print("Enter a positive number")