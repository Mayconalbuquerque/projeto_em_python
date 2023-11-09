def multiplication(*args):
    total = 1

    for number in args:
        total = total * number
    print(total)
    return oddoreven(total)

def oddoreven(number):
    if (number % 2) == 0:
        print('This number is even!')

    else:
        print('This number is odd') 

numbers = 1, 2, 3
last_multiplier = multiplication(*numbers)
print(last_multiplier)