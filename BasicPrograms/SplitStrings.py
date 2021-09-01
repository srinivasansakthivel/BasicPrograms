str1 = "A B C D E F G H"
data = str1.split(" ", 2)
length_data = len(data)
print(length_data)

for i in data:
    print(i)
print(data[0])
print(data[1])
print(data[2])

str2 = "     Hello World New      "
print(str2.strip())
