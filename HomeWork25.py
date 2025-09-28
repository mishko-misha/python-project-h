from typing import Iterator, Callable


def pow(x):
    return x ** 2


def some_gen(begin: int, end: int, func: Callable[[int], int]) -> Iterator[int]:
    """
     begin: first element sequence
     end: number of elements in sequence
     func: function that forms values for the sequence
    """
    for _ in range(end):
        yield begin
        begin = func(begin)


# from inspect import isgenerator
#
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
