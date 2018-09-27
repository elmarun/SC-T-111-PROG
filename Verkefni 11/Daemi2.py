#list_to_tuple function goes here
def list_to_tuple(listi):
    try:
        new_list = []
        for i in listi:
            new_list.append(int(i))
        return tuple(new_list)
    except Exception:
        print("Error. Please enter only integers.")
        return tuple()

# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)
