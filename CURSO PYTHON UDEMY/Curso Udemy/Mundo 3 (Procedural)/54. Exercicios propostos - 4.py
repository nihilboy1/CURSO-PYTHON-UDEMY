def fizzbuzz(a):
    if a % 3 == 0 and a % 5 == 0:
        return 'fizzbuzz'
    elif a % 3 == 0:
        return 'fizz'
    elif a % 5 == 0:
        return 'buzz'
    else:
        return a


print(fizzbuzz(9))
