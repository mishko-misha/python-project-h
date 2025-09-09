import random

my_list = [random.randint(3, 100) for i in range(random.randint(3, 10))]
new_random_list = [my_list[0], my_list[2], my_list[-2]]
print(new_random_list)
