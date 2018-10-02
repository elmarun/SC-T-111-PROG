#game_of_eights() function goes here
def game_of_eights(listi: int):
    try:
        attur = []
        for x in listi:
            if x == 8:
                attur.append(x)

        if len(attur) >= 2:
            return True
        else:
            return False

    except ValueError:
        print("Error. Please enter only integers.")


def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    # remainder of main() goes here
    print(game_of_eights(a_list))


main()
