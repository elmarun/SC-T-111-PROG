# Your function definition goes here
def f(n):
    if n <= 1:
        return n
    else:
        return f(n-1) + f(n-2)


num = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here

if num >= 0:
    for i in range(1, num + 1):
        print(f(i), end=" ")
