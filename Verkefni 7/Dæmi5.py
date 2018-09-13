in_str = input("Enter a string: ")


def palindrome(word):
    new_word = word.replace("'", '').replace('!', '').replace(' ', '').replace(',', '').lower()
    if new_word == new_word[::-1]:
        return True
    else:
        return False


if palindrome(in_str):
    print('"' + in_str + '"', "is a palindrome.")
else:
    print('"' + in_str + '"', "is not a palindrome.")
