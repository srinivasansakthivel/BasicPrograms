import math
def compute_gcd(a, b):
    if b == 0:
        return a
    else:
        return compute_gcd(b, a % b)


num1 = int(input("Enter the num1 value : "))
num2 = int(input("Enter the num2 value : "))
result = compute_gcd(num1, num2)
print("GCD of two numbers is : ", result)
print(math.gcd(16,18))



