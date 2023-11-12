def filter_negative_numbers(numbers: list):
    result = []
    for num in numbers:
        if num >= 0:
            result.append(num)
    return result


print(filter_negative_numbers([6, -5, 0, -1, 100]))
print(filter_negative_numbers([9, 2, -5, -3, 7, 0]))