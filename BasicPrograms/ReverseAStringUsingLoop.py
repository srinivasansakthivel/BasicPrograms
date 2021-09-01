def reversing_string(string):
    reverse_string = ""
    for i in string:
        reverse_string = i + reverse_string
    return reverse_string


string1 = input("Enter the string : ")
rev_string1 = reversing_string(string1)
print(rev_string1)
