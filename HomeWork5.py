my_list = []

if my_list:
    last_number = my_list[-1]
    x = my_list.pop(-1)
    my_list.insert(0, last_number)
else:
    my_list = []

print(my_list)