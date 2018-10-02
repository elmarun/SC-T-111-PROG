#game_of_eights() function goes here
def game_of_eights(a_list):
    check = [letter for letter in a_list if letter.isalpha()]
    if len(check) > 0:
        return "Error. Please enter only integers."
    else:
        i = 0
        for number in a_list:
            if i+1 == len(a_list):
                return False
            elif int(number) == 8 and int(a_list[i+1]) == 8:
                return True
            i += 1
        return False
def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    # remainder of main() goes here
    print (game_of_eights(a_list))
main()
