strating_pont = 1.1


while position != 3.1:
    direction = input("Direction: ")
    if position == 3.1:
        print("Victory!")
        break
    elif direction == 'n':
        position += 0.1
    elif direction == 's':
        position -= 0.1
    elif direction == 'w':
        position += 1.0
    elif direction == 'e':
        position = -= 1.0 
    else:
        break

if position == 1.1:
    posible_travel = "(N)orth."
if position == 1.2:
    posible_travel = "(N)orth or (W)est or (S)outh."
if position == 2.2:
    posible_travel = "(E)ast or (S)outh."
if position == 2.1:
    posible_travel = "(N)orth."
if position == 1.3:
    posible_travel = "(N)orth or (S)outh."
if position == 2.3:
    posible_travel = "(E)ast or (W)est."
if position == 3.3:
    posible_travel = "(E)ast or (S)outh."
if position == 3.2:
    posible_travel = "(N)orth or (S)outh."


print("You can travel:",posibletravel)
