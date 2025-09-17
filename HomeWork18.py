def second_index(text, some_str):
    first_symbol = text.find(some_str)
    second_symbol = text.find(some_str, first_symbol + 1)
    if second_symbol == -1:
        return None
    return second_symbol
print('ОК')

# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
