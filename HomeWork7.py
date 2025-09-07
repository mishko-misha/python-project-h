numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
i = 0
length = len(numbers)

while i < length:
    if numbers[i] == 0:
        numbers.pop(i)
        numbers.append(0)
        length -= 1
    else:
        i += 1
print(numbers)