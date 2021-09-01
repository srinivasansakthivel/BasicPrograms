def fact(n):
    if n >= 0:
        if n==0:
            return 1
        else:
            return n*fact(n-1)
    else:
        print("Enter a positive number")


num = int(input("Enter the number to find the factorial : "))
result = fact(num)
print(f"Factorial of {num} is {result}")
