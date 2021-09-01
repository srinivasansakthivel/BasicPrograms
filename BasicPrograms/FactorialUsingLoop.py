num = int(input("Enter the number to find the factorial : "))
result = 1
for i in range(num, 0 , -1):
    result = result * i
print(f"Factorial of {num} is {result}")