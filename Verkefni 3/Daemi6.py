number = 10
while number < 100:
    three_digits = number * number
    three_str = str(three_digits)
    last_two = three_str[1:]
    number_str = str(number)

    if last_two == number_str:
        print (number)

    number += 1
