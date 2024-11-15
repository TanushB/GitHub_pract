def calculate_average(numbers):
    sum = 0
    for i in range(0, len(numbers)):
        sum = sum + numbers[i]
    if len(numbers) > 0:
        return sum / len(numbers)
    else:
        return None
