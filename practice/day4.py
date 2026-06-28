def get_stats(numbers):
    count = len(numbers)
    total = sum(numbers)
    average = total / count if count > 0 else 0
    return {'count': count, 'sum': total, 'average': average}

print(get_stats([1, 2, 3, 4, 5]))  # {'count': 5, 'sum': 15, 'average': 3.0}

print(get_stats([]))  # {'count': 0, 'sum': 0, 'average': 0}