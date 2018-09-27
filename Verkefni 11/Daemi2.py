#list_to_tuple function goes here
def list_to_tuple(listi):
    for x in listi:
        if x.isalpha():
            print("Error. Please enter only integers.")
            return tuple()
    return tuple(listi)


# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)
