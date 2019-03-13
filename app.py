def fizz_buzz(input):
    div_by_3 = input % 3 == 0
    div_by_5 = input % 5 == 0

    if div_by_3 and div_by_5:
        print('fizzbuzz')
    elif div_by_3:
        print('fizz')
    elif div_by_5:
        print('buzz')
    else:
        print(input)


fizz_buzz(16)
