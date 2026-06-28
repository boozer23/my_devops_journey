def filter_numbers(numbers):
    result = []
    for num in numbers:
        if num > 50:
            result.append(num)
    return result


nums = [10, 55, 3, 80, 47, 51, 100]
print(filter_numbers(nums))  # [55, 80, 51, 100]
