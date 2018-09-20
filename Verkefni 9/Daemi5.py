with open("words.txt", "r") as rf:
    for line in rf:
        stripped = line.strip().replace('.', '\n')
        print(stripped, end=" ")

    with open("sentences.txt", "w") as w:
        w.write(stripped)
