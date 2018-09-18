pos = 1.1
travel = "(N)orth"
print("You can travel: ", travel)

while True:
    direction = input("Direction: ").lower()

    round_pos = round(pos, 1)
    #print(round_pos)

    if round_pos == 3.1:
        print("Victory!")
        break

    if round_pos == 1.1:
        if direction != "n":
            print("Not a valid direction!")
            pos = pos
            continue
        travel = "(N)orth"
    elif round_pos == 1.2:
        travel = "(N)orth or (W)est or (S)outh."
        if direction == "e":
            print("Not a valid direction!")
            continue
    elif round_pos == 2.2:
        travel = "(E)ast or (S)outh."
        if direction == "n" or direction == "w":
            print("Not a valid direction!")
            continue
    elif round_pos == 2.1:
        travel = "(N)orth."
        if direction != "n":
            print("Not a valid direction!")
            continue
    elif round_pos == 1.3:
        travel = "(E)ast or (S)outh."
        if direction == "n" or direction == "w":
            print("Not a valid direction!")
            continue
    elif round_pos == 2.3:
        travel = "(E)ast or (W)est."
        if direction == "n" or direction == "s":
            print("Not a valid direction!")
            continue
    elif round_pos == 3.3:
        travel = "(S)outh or (W)est."
        if direction == "n" or direction == "e":
            print("Not a valid direction!")
            continue
    elif round_pos == 3.2:
        travel = "(N)orth or (S)outh."
        if direction == "e" or direction == "w":
            print("Not a valid direction!")
            continue
    print("You can travel: ", travel)

    if direction == "n":
        pos += 0.1
    elif direction == "s":
        pos -= 0.1
    elif direction == "w":
        pos -= 1.0
    elif direction == "e":
        pos += 1.0
    else:
        print("Not a valid direction!")


