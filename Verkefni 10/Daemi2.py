def to_list(st):
    arr = []
    stri = st.replace(",", " ").split(" ")
    for x in stri:
        arr.append(x)
    return arr


the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)
