n = int(input("Enter the number to check whether it is Armstrong Number or Not : "))
actual_number = n
if n > 0:
    length_n = len(str(n))
    result = 0
    while n >= 1:
        digit = n % 10
        print(digit)
        result = result + (digit**length_n)
        n = n // 10
    print("Result: ", result)
    print("Actual Number : ", actual_number)
    if result == actual_number:
        print("Given number is Armstrong Number")
    else:
        print("Not an Armstrong Number")
else:
    print("Enter a positive number greater then zero")