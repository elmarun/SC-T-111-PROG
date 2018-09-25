# Your functions should appear here
def populate_list(l):
    while True:
        val = input("Enter value to be added to list: ")
        if val.lower() == "exit":
            break
        else:
            l.append(val)
    return l


def triple_list(l):
    return l*3


# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
