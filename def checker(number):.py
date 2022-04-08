def checker(number):
    try:
        number = int(number)
        if number % 2 == 0:
            print('четное')
        if number % 2 != 0:
            print('нечетное')
    except:
        print('этот символ не номер')

checker(13)