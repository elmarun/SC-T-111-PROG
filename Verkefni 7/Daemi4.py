# is_prime function definition goes here
def is_prime(x):
    if x != 2 and x%2 == 0 or x%3 == 0:
        return False
    else:
        return True


num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message

if is_prime(num):
    print(num, "is a prime")
else:
    print(num, "is not a prime")
