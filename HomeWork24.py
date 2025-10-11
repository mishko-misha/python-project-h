from typing import Union


def difference(*args: Union[int, float]) -> Union[int, float]:
    """
    :param args: tuple numerically int or float
    :return: difference int or float, 0 if no arguments
    """
    if not args:
        return 0
    diff = max(args) - min(args)
    return round(diff, 2)


# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
print('OK')
