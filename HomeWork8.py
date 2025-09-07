numbers = [0, 1, 7, 2, 4, 8]
result = 0

for i in range(0, len(numbers), 2):
    result += numbers[i] * numbers[-1]
print(result)