position = 1.1
posible_travel = "(N)orth."

while position != 3.1:
    print("You can travel:", posible_travel)
    print(position)
    direction = input("Direction: ").lower()
    
    elif position == 1.2:
        posible_travel = "(N)orth or (E)ast or (S)outh."
        direction = input("Direction: ").lower()
    elif position == 2.2:
        posible_travel = "(W)est or (S)outh."
    elif position == 2.1:
        posible_travel = "(N)orth."
    elif position == 1.3:
        posible_travel = "(E)east or (S)outh."
    elif position == 2.3:
        posible_travel = "(E)ast or (W)est."
    elif position == 3.3:
        posible_travel = "(W)est or (S)outh."
    elif position == 3.2:
        posible_travel = "(N)orth or (S)outh."

    elif direction == 'n':
        position += round(0.1, 1)
    elif direction == 's':
        position -= round(0.1, 1)
    elif direction == 'w':
        position -= round(1.0, 1)
    elif direction == 'e':
        position += round(1.0, 1)

    elif position == 3.1:
        print("Victory!")
        break

