d1 = int(input("Input first dice: "))  # Do not change this line
d2 = int(input("Input second dice: "))  # Do not change this line

# Fill in the missing code below

if d1 > 6 or d1 < 1 or d2 > 6 or d2 < 1:
    print("Invalid input")
else:
    sums = d1 + d2
    if sums == 7 or sums == 11:
        print("Winner")
    elif sums == 2 or sums == 3 or sums == 12:
        print("Loser")
    else:
        print("Your sum is: ", sums)
