with open("test.txt", "r") as rf:
    for line in rf:
        stripped = line.strip().replace(' ', '')
        print(stripped, end="")
