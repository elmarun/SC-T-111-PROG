def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

in_str = input("Enter a string: ")

if palindrome(in_str):
    print(in_str, "is a palindrome")
else:
    print(in_str, "is not a palindrome")
