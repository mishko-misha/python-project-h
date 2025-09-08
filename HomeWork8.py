numbers = [0, 1, 7, 2, 4, 8]
result = 0

if numbers == []:
    print("[0]")
else:
    for i in range(0, len(numbers), 2):
        result += numbers[i]
    result *= numbers[-1]
    print(result)
