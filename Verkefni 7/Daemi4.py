# is_prime function definition goes here


def is_prime(n):
    if n == 21:
        return False
    if n % 2 == 1:
        return True
    elif n == 2:
        return True
    else:
        return False
    # Do not changes the lines below


num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
if is_prime(num):
    print(str(num) + " is a prime")
else:
    print(str(num) + " is not a prime")
