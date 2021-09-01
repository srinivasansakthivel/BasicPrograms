user_str = input("Enter the String : ")
# rev_str = user_str[::-1]
# if user_str == rev_str:
#     print("It is palindrome")
# else:
#     print("Not a palindrome")


# without using reverse func
rev_str = ""
for i in range(len(user_str)-1, -1, -1):
    rev_str = user_str[i] + rev_str
print("Reversed String : ", rev_str)
if user_str == rev_str:
    print("It is palindrome")
else:
    print("Not a palindrome")



