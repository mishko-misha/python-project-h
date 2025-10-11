def prime_generator(end: int):
    """
    :param end: upper limit of range
    :return: generator which returns range of numbers from 2 to end
    """
    for num in range(2, end + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
