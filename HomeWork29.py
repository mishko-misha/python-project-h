def generate_cube_numbers(end: int):
    """
    :param end: upper limit of range
    :return: generator which returns cubes of numbers from 2 to end
    """
    i = 2
    while True:
        cube = i ** 3
        if cube > end:
            return
        yield cube
        i += 1
    # without return better
    # while i ** 3 <= end:
    #     yield i ** 3
    #     i += 1


from inspect import isgenerator

gen = generate_cube_numbers(1000)
assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
