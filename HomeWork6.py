my_list = [1, 2, 3, 4, 5, 6, 7]
size_my_list = len(my_list)

first_part = my_list[:size_my_list//2 + size_my_list%2]
second_part = my_list[size_my_list//2 + size_my_list%2:]
print([first_part, second_part])