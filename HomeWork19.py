def common_elements():
    my_list_one = set(range(0, 100, 3))
    my_list_two = set(range(0, 100, 5))
    intersection_set = my_list_one.intersection(my_list_two)
    return intersection_set

# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}