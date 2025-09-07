numbers = [0, 1, 7, 2, 4, 8]
even_index_numbers = 0
result = 0

for i in range(0, len(numbers), 2):
    even_index_numbers += numbers[i]
    result = even_index_numbers * numbers[-1]
print(result)
