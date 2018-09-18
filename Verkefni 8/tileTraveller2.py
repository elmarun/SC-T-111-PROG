pos = 1.1
travel = "(N)orth."
no_print = True


def check_victory(p):
    """
    :param p:
    :return:
    """
    if p == 3.1:
        print("Victory!")
        quit()


def east(p, pr):
    if p == 1.1 or p == 2.2 or p == 3.3 or p == 3.2 or p == 2.1 or p == 3.1:
        print("Not a valid direction!")
        pr = False
    else:
        p += 1.0
        pr = True
    return p, pr


def west(p, pr):
    if p == 1.1 or p == 1.2 or p == 2.1 or p == 1.3 or p == 3.2 or p == 3.1:
        print("Not a valid direction!")
        pr = False
    else:
        p -= 1.0
        pr = True
    return p, pr


def north(p, pr):
    if p == 1.3 or p == 2.3 or p == 3.3 or p == 2.2:
        print("Not a valid direction!")
        pr = False
    else:
        p += 0.1
        pr = True
    return p, pr


def south(p, pr):
    if p == 1.1 or p == 2.1 or p == 2.3 or p == 3.1:
        print("Not a valid direction!")
        pr = False
    else:
        p -= 0.1
        pr = True
    return p, pr


def check_direction(d, p, pr):
    if d == "n":
        return north(p, pr)
    elif d == "s":
        return south(p, pr)
    elif d == "w":
        return west(p, pr)
    elif d == "e":
        return east(p, pr)
    else:
        print("Not a valid direction!")


def check_possible_directions(t):
    if round_pos == 1.1:
        t = "(N)orth."
    elif round_pos == 1.2:
        t = "(N)orth or (E)ast or (S)outh."
    elif round_pos == 2.2:
        t = "(S)outh or (W)est."
    elif round_pos == 2.1:
        t = "(N)orth."
    elif round_pos == 1.3:
        t = "(E)ast or (S)outh."
    elif round_pos == 2.3:
        t = "(E)ast or (W)est."
    elif round_pos == 3.3:
        t = "(S)outh or (W)est."
    elif round_pos == 3.2:
        t = "(N)orth or (S)outh."
    return t


while True:
    round_pos = round(pos, 1)

    check_victory(round_pos)

    travel = check_possible_directions(travel)

    if no_print:
        print("You can travel:", travel)

    direction = input("Direction: ").lower()

    pos, no_print = check_direction(direction, round_pos, no_print)
