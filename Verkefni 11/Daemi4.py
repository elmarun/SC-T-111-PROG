def get_emails():
    listi = []
    while True:
        i = input("Email address: ").lower()
        if i == "q":
            break

        listi.append(i)
    return listi


def get_names_and_domains(email):
    tup = []
    for element in email:
        split_email = element.split("@")
        tup.append(tuple(split_email))
    return tup


# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)
