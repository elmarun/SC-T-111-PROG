def merge_lists(l1, l2):
    listi = []
    for x in l1:
        if x not in listi:
            listi.append(x)
    for y in l2:
        if y not in listi:
            listi.append(y)

    return sorted(listi)


# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
