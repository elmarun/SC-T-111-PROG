import string


#build_wordlist() function goes here
def build_wordlist(file_name):
    with open(file_name, "r", encoding="utf-8") as dataFile:
        word_string = ''     # start with an empty string of words
        for line in dataFile:
            word_string += line.strip(string.punctuation).replace("\n", " ")  # add each line of words to the word string
    return list(word_string.split(" "))


#find_unique() function goes here
def find_unique(words):
    output = []
    for x in words:
        if x not in output:
            output.append(x)
    return output


def main():
    infile = "test.txt"
    word_list = build_wordlist(infile)
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)


main()
