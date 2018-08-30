top_num = int(input("Upper number for the range: ")) # Do not change this line

for c in range(1, top_num):
    if sum(x for x in range(1, c) if not c % x) == c:
        print(c)
