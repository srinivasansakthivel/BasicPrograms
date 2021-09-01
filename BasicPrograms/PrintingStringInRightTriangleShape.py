user_str = input("Enter the string : ")
len_user_str = len(user_str)
for row in range(len_user_str):
    for col in range(row+1):
        print(user_str[col], end=" ")
    print()
