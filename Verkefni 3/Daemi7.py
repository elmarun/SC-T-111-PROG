counter = 1
while counter <= 18:
    par = int(input("Par of hole " + str(counter) + ": "))
    i = int(input("Score on hole " + str(counter) + ": "))

    if i < (par - 3):
        print("invalid score")
    elif i == (par - 3):
        print("albatross")
    elif i == (par - 2):
        print("eagle")
    elif i == (par - 1):
        print("birdie")
    elif i == (par + 1):
        print("bogey")
    elif i == (par + 2):
        print("double bogey")
    elif i == (par + 3):
        print("triple bogey")
    elif i > (par + 3):
        print("bad hole")
    else:
        print("par")

    counter = counter + 1