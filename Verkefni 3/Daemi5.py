n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
while True:
    if n % 2 == 1:
        prime = True
        break
    elif n == 2:
        prime = True
        break
    else:
        prime = False
        break
# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("!Prime")