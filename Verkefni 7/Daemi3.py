# The function definition goes here


def inrange(n):
    if 1 < n < 555:
        return True
    else:
        return False


num = int(input("Enter a number: "))

# You call the function here
if inrange(num):
    print(str(num) + " is in range.")
else:
    print(str(num) + " is outside the range!")
