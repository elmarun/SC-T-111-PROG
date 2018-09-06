name = input("Input a name: ")

first, last = name.split(', ')

fnam = last[0].upper()
flname = first[0].upper()
print(fnam + '. ' + flname + first[1::])
