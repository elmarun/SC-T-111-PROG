s = input("Input a string: ")
arr = []
for char in s:
    if char.isdigit():
        arr.append(char)
print(''.join(arr))
